import streamlit as st
import tempfile
import os
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Align import MultipleSeqAlignment
from itertools import combinations
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

def msa_ui():
    #st.image("logo.png", width=150)
    #st.markdown("## My Bioinformatics App")

    def plot_base_frequencies(alignment):
        base_counts = Counter()
        for record in alignment:
            base_counts.update(record.seq)

        bases = list(base_counts.keys())
        counts = [base_counts[base] for base in bases]

        fig, ax = plt.subplots()
        sns.barplot(x=bases, y=counts, ax=ax)
        ax.set_title("Base Frequencies")
        ax.set_xlabel("Base")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    def plot_dotplot(seq1, seq2, window=1):
        matches = []
        for i in range(len(seq1) - window + 1):
            for j in range(len(seq2) - window + 1):
                if seq1[i:i+window] == seq2[j:j+window]:
                    matches.append((i, j))

        x, y = zip(*matches) if matches else ([], [])
        fig, ax = plt.subplots()
        ax.plot(x, y, 'k.', markersize=2)
        ax.set_xlabel("Sequence 1")
        ax.set_ylabel("Sequence 2")
        ax.set_title("Dot Plot")
        st.pyplot(fig)


    def generate_alignment_report(alignment, formatted_alignment, stats):
        report = StringIO()
        report.write("### Alignment Statistics\n")
        report.write(f"Alignment Length: {stats['alignment_length']}\n")
        report.write(f"Average Pairwise Identity: {stats['average_identity']:.2f}%\n")
        report.write(f"Average Gaps per Pair: {stats['average_gaps']}\n")
        report.write(f"Total Sequences: {len(alignment)}\n\n")
        report.write("### Visual Alignment\n")
        report.write(formatted_alignment)
        return report

    def plot_identity_heatmap(alignment):
        labels = [record.id for record in alignment]
        n = len(alignment)
        matrix = np.zeros((n, n))

        for i, rec1 in enumerate(alignment):
            for j, rec2 in enumerate(alignment):
                if i <= j:
                    matches = sum(a == b and a != '-' for a, b in zip(rec1.seq, rec2.seq))
                    identity = matches / len(rec1.seq) * 100
                    matrix[i, j] = identity
                    matrix[j, i] = identity  # symmetric
        df = pd.DataFrame(matrix, index=labels, columns=labels)

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df, annot=True, fmt=".1f", cmap="viridis", ax=ax)
        ax.set_title("Pairwise Identity (%)")
        st.pyplot(fig)


    def plot_pairwise_identities(stats):
        fig, ax = plt.subplots()
        ax.hist(stats["pairwise_identities"], bins=10, color='teal', edgecolor='black')
        ax.set_title("Pairwise Identity Distribution")
        ax.set_xlabel("Identity (%)")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    #st.title("🧩 Multiple Sequence Alignment (MSA)")

    st.title("Multiple Sequence Alignment (MSA)")
    st.markdown("""Upload multiple FASTA files **or** paste multiple sequences below:
    	    Results and alignment plots can be downloaded.""")

    # Input methods
    msa_files = st.file_uploader("Upload FASTA files", type=["fasta", "fa"], accept_multiple_files=True)
    sequence_text = st.text_area("Or paste multiple FASTA sequences here", height=300)

    run_button = st.button("Run MSA")

    def compute_alignment_stats(alignment: MultipleSeqAlignment):
        stats = {
            "alignment_length": alignment.get_alignment_length(),
            "pairwise_identities": [],
            "pairwise_gaps": [],
        }

        for rec1, rec2 in combinations(alignment, 2):
            matches = sum(a == b and a != '-' for a, b in zip(rec1.seq, rec2.seq))
            gaps = sum(a == '-' or b == '-' for a, b in zip(rec1.seq, rec2.seq))
            length = len(rec1.seq)

            identity = (matches / length) * 100
            stats["pairwise_identities"].append(identity)
            stats["pairwise_gaps"].append(gaps)

        stats["average_identity"] = sum(stats["pairwise_identities"]) / len(stats["pairwise_identities"])
        stats["average_gaps"] = sum(stats["pairwise_gaps"]) / len(stats["pairwise_gaps"])
        return stats

    #from Bio.Align import MultipleSeqAlignment

    def format_alignment_with_symbols(alignment: MultipleSeqAlignment, line_width=60) -> str:
        """
        Formats DNA alignment with:
        - '|' for exact match
        - ':' for similar (purine↔purine or pyrimidine↔pyrimidine)
        - ' ' for mismatches/gaps
        """

        purines = {'A', 'G'}
        pyrimidines = {'C', 'T'}

        output = ""
        alignment_len = alignment.get_alignment_length()

        for block_start in range(0, alignment_len, line_width):
            block_end = min(block_start + line_width, alignment_len)

            # Sequence block
            seq_lines = [
                f"Seq{i+1:<4} {str(record.seq[block_start:block_end])}"
                for i, record in enumerate(alignment)
            ]

            # Match line
            match_line = []
            for pos in range(block_start, block_end):
                column = [record.seq[pos] for record in alignment]
                if '-' in column:
                    match_line.append(" ")
                    continue

                if all(base == column[0] for base in column):
                    match_line.append("|")
                elif all(base in purines for base in column) or all(base in pyrimidines for base in column):
                    match_line.append(":")
                else:
                    match_line.append(" ")

            output += "\n".join(seq_lines) + "\n"
            output += "    " + "    " + "".join(match_line) + "\n\n"  # Add 3+3=6 spaces for alignment

        return output



    if run_button:
        try:
            # Step 1: Write sequences to a temporary file
            if sequence_text.strip():
                input_data = sequence_text.strip()
            elif msa_files:
                input_data = ""
                for file in msa_files:
                    input_data += file.read().decode() + "\n"
            else:
                st.warning("Please upload FASTA files or paste sequences.")
                st.stop()

            with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".fasta") as input_file:
                input_file.write(input_data)
                input_file.flush()

                aligned_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".fasta")

                # Step 2: Run Clustal Omega
                clustal_cmd = ClustalOmegaCommandline(
                    infile=input_file.name,
                    outfile=aligned_file.name,
                    auto=True,
                    force=True
                )
                stdout, stderr = clustal_cmd()

                # Step 3: Display results
                alignment_obj = AlignIO.read(aligned_file.name, "fasta")
                #alignment = open(aligned_file.name).read()
                st.success("Alignment completed successfully.")
                
                # Show raw alignment
                st.code(open(aligned_file.name).read(), language="fasta")
                
                # Show the aligned sequences in symbolic form
                formatted = format_alignment_with_symbols(alignment_obj)
                st.text_area("🧬 Visual Alignment", formatted, height=500)
                # Compute and display stats
                stats = compute_alignment_stats(alignment_obj)
                

                #st.download_button("⬇️ Download Alignment Report", export_text.getvalue(), file_name="alignment_report.txt")

                # 🔳 Identity matrix heatmap
                st.markdown("### 🧊 Pairwise Identity Heatmap")
                plot_identity_heatmap(alignment_obj)
                
                
                # ➖ Dot plot comparisons (for 2 sequences at a time)
                st.markdown("### 🔲 Dot Plots (Pairwise)")
                from itertools import combinations
                for i, j in combinations(range(len(alignment_obj)), 2):
                    st.markdown(f"**Seq{i+1} vs Seq{j+1}**")
                    plot_dotplot(str(alignment_obj[i].seq), str(alignment_obj[j].seq))
                    plot_pairwise_identities(stats)
                
                # 📉 Base or amino acid frequencies
                st.markdown("### 🔢 Base / Amino Acid Frequencies")
                plot_base_frequencies(alignment_obj)
                
                
                
                st.markdown("### 📊 Alignment Statistics")
                st.markdown(f"""
                - **Alignment Length:** {stats['alignment_length']}  
                - **Average Pairwise Identity:** {stats['average_identity']:.2f}%  
                - **Average Gaps per Pair:** {stats['average_gaps']}  
                - **Total Sequences:** {len(alignment_obj)}
                """)
                # Download: Aligned FASTA
                with open(aligned_file.name, "rb") as f:
                    st.download_button("⬇️ Download Aligned FASTA", f, file_name="aligned_sequences.fasta")
                # Download: Stats + Visual Alignment as TXT
                from io import StringIO
                export_text = StringIO()
                export_text.write("### Alignment Statistics\n")
                export_text.write(f"Alignment Length: {stats['alignment_length']}\n")
                export_text.write(f"Average Pairwise Identity: {stats['average_identity']:.2f}%\n")
                export_text.write(f"Average Gaps per Pair: {stats['average_gaps']}\n")
                export_text.write(f"Total Sequences: {len(alignment_obj)}\n\n")
                export_text.write("### Visual Alignment\n")
                export_text.write(formatted)
                
                report = generate_alignment_report(alignment_obj, formatted, stats)
                st.download_button("⬇️ Download Alignment Report",data=export_text.getvalue(), file_name="alignment_report.txt",mime="text/plain")


        except Exception as e:
            st.error(f"An error occurred while running MSA:\n\n{str(e)}")

