# Mango Genome Database & Comparative Genomics Platform

Welcome to the **Mango Genome Database**, a comprehensive and interactive platform built using **Streamlit**, designed to:

- Perform **BLAST** searches against mango genome/proteome datasets
- Run **Multiple Sequence Alignments (MSA)** with MUSCLE
- Download curated reference datasets
- Learn about the mango genome and related literature

> ⚠️ **This app is intended for local use only** as it depends on system-level tools: NCBI BLAST+ and MUSCLE.

---

## 🧰 Features

- 🔍 Nucleotide and protein **BLAST** using pre-indexed databases
- 🧬 **MSA** functionality with easy-to-use interface
- 📥 Genome downloads
- 🧾 Informative "About" and "Help" sections

---

## 📦 Requirements

### 🖥️ System Tools

Install these tools **before** running the app:

- [NCBI BLAST+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
- [MUSCLE](https://www.drive5.com/muscle/)

Ensure they are added to your system `PATH`.

### 🐍 Python Environment

Python 3.8 or newer

```bash
pip install -r requirements.txt
```


---

## 🚀 Installation & Running

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/mango-genome-database.git
cd mango-genome-database
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install NCBI BLAST+ and MUSCLE

**Ubuntu/Linux:**

```bash
sudo apt install ncbi-blast+
sudo apt install muscle
```

**Windows/Mac:**

- Download BLAST+ and MUSCLE binaries manually
- Add them to your system `PATH`

### Step 4: Verify Installation

```bash
blastn -version
blastp -version
muscle -version
```

---

## 📁 Directory Structure

```
mango_genome_comparator/
├── app.py                  # Streamlit main script
├── blast.py                # BLAST module
├── msa.py                  # MSA module
├── db/                     # BLAST+ databases (.nsq, .nin, .psq, etc.)
├── static/Images/          # UI images
├── static/SSUETLogo.png    # Institute logo
├── logo.png                # App logo
├── input.fasta             # Example input
├── __pycache__/            # Cache
```

---

## ▶️ Running the App

From the root directory:

```bash
streamlit run app.py
```

Open the generated **localhost** link in your browser.

---

## 🔧 Adding New Databases

To add a new FASTA file to the database:

```bash
makeblastdb -in my_sequences.fasta -dbtype nucl -out db/my_new_db
```

Use `-dbtype prot` for protein sequences.

Ensure the database files are placed in the `db/` folder.

---

## ❓ Support

**Department of Bioinformatics**\
Sir Syed University of Engineering & Technology, Karachi\
📧 Email: [qamartayyaba@yahoo.com](mailto\:qamartayyaba@yahoo.com)\
📞 Phone: +92 336 2808926

**Development Team — BioInfoQuant**\
📧 Email: [contact@bioinfoquant.com](mailto\:contact@bioinfoquant.com)\
🌐 Website: [https://www.bioinfoquant.com](https://www.bioinfoquant.com)

---

## 📄 License

This project is for **academic and research use only**.\
All rights reserved © BioInfoQuant & SSUET, 2025.

