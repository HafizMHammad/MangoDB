import streamlit as st
import subprocess
import tempfile
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

def blast_ui():
    #st.image("logo.png", width=150)
    #st.markdown("## My Bioinformatics App")

    #st.title("🧬 BLAST Search")

    st.title("BLAST Search")
    st.markdown("""Upload or paste your sequence to perform BLAST search.
    Choose between nucleotide BLAST (blastn) or protein BLAST (blastp).
    Select the database from 'All Genomes' or specific genome datasets.
    Results can be downloaded in CSV or TSV formats.""")

    # Input methods
    uploaded_file = st.file_uploader("Upload your FASTA file", type=["fasta", "fa"])
    sequence_text = st.text_area("Or paste your FASTA sequence here", height=200)

    blast_type = st.selectbox("Select BLAST type", ["blastn", "blastp"])

    # Get DBs
    db_dir = "db"
    db_files = os.listdir(db_dir)
    db_suffix = ".nsq" if blast_type == "blastn" else ".psq"
    label = "All Genomes" if blast_type == "blastn" else "All Proteomes"

    # Build DB list
    db_names = sorted({f.split(".")[0] for f in db_files if f.endswith(db_suffix)})
    if label not in db_names:
        db_names.insert(0, label)  # Prepend 'All' option
    db_choice = st.selectbox("Choose Database", db_names, index=0)  # default to 'All'

    def gc_content(seq):
        seq = seq.upper()
        gc_count = seq.count("G") + seq.count("C")
        return round(gc_count / len(seq) * 100, 2) if len(seq) > 0 else 0

    run_button = st.button("Run BLAST")

    if run_button:
        if sequence_text.strip():
            input_data = sequence_text.strip()
        elif uploaded_file:
            input_data = uploaded_file.read().decode()
        else:
            st.warning("Please upload a FASTA file or paste a sequence.")
            st.stop()

        # Basic stats
        lines = input_data.splitlines()
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]
        query_seq = "".join(seq_lines)
        seq_len = len(query_seq)
        gc = gc_content(query_seq)

        st.markdown(f"**Query sequence length:** {seq_len} bp")
        st.markdown(f"**GC content:** {gc} %")
        st.info("Running BLAST, please wait...")

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as query_file:
            query_file.write(input_data)
            query_file.flush()

            blast_output = tempfile.NamedTemporaryFile(mode='w+', delete=False)

            # DB path
            db_path = os.path.join(db_dir, label.replace(" ", "_").lower()) if db_choice == label else os.path.join(db_dir, db_choice)

            result = subprocess.run(
                [blast_type, "-query", query_file.name, "-db", db_path,
                "-outfmt", "6", "-evalue", "1e-5", "-out", blast_output.name],
                capture_output=True, text=True
            )

            if result.returncode != 0:
                st.error("Error running BLAST:\n" + result.stderr)
            else:
                output_text = open(blast_output.name).read()
                if not output_text.strip():
                    st.warning("No hits found.")
                else:
                    st.success("BLAST completed.")

                    colnames = ["Query ID", "Subject ID", "% Identity", "Alignment Length", "Mismatches",
                                "Gap Openings", "Query Start", "Query End", "Subject Start", "Subject End",
                                "E-value", "Bit Score"]
                    df = pd.read_csv(blast_output.name, sep="\t", names=colnames)

                    st.subheader("BLAST Hits Table")
                    st.dataframe(df)

                    # Download raw & parsed
                    #st.download_button(
                    #    label="Download Raw BLAST Output",
                    #    data=output_text,
                    #    file_name="blast_output.tsv",
                    #    mime="text/tab-separated-values"
                    #)
                    csv_buffer = df.to_csv(index=False)
                    st.download_button(
                        label="Download Parsed Results (CSV)",
                        data=csv_buffer,
                        file_name="blast_results.csv",
                        mime="text/csv"
                    )

                    st.subheader("Alignment Statistics Plots")

                    def save_and_show_plot(fig, title, filename):
                        st.pyplot(fig)
                        buf = io.BytesIO()
                        fig.savefig(buf, format='png')
                        buf.seek(0)
                        st.download_button(
                            label=f"Download {title} as PNG",
                            data=buf,
                            file_name=filename,
                            mime="image/png"
                        )

                    # 1. Identity %
                    fig1, ax1 = plt.subplots(figsize=(10, 5))
                    ax1.hist(df["% Identity"], bins=20, color="skyblue", edgecolor="black")
                    ax1.set_title("% Identity Distribution")
                    ax1.set_xlabel("% Identity")
                    ax1.set_ylabel("Count")
                    plt.tight_layout()
                    save_and_show_plot(fig1, "Identity Plot", "percent_identity.png")

                    # 2. E-value (-log10)
                    fig2, ax2 = plt.subplots(figsize=(10, 5))
                    evalues = df["E-value"].replace(0, 1e-180)
                    ax2.hist(-np.log10(evalues), bins=20, color="salmon", edgecolor="black")
                    ax2.set_title("Log10(E-value) Distribution")
                    ax2.set_xlabel("-log10(E-value)")
                    ax2.set_ylabel("Count")
                    plt.tight_layout()
                    save_and_show_plot(fig2, "E-value Plot", "evalue_log10.png")

                    # 3. Bit Score
                    fig3, ax3 = plt.subplots(figsize=(10, 5))
                    ax3.hist(df["Bit Score"], bins=20, color="lightgreen", edgecolor="black")
                    ax3.set_title("Bit Score Distribution")
                    ax3.set_xlabel("Bit Score")
                    ax3.set_ylabel("Count")
                    plt.tight_layout()
                    save_and_show_plot(fig3, "Bit Score Plot", "bit_score.png")

