# 🧬 Identification of Anti-Ageing Biomarkers Using Transcriptomic Data

This repository contains the computational analysis pipeline, figures, and LaTeX thesis files for the M.Sc. Bioinformatics dissertation titled:

**Identification of Anti-Ageing Biomarkers in Humans Using Transcriptomic Data**

The study investigates age-associated transcriptomic changes in human primary skin fibroblasts using publicly available RNA-sequencing data and a reproducible Python-based bioinformatics workflow.

---

## 🎓 Academic Details

- **Degree:** Master of Science (M.Sc.) in Bioinformatics  
- **University:** Pondicherry University, Puducherry, India  
- **Student:** Ankur Kumar  
- **Registration Number:** 24MSBINPY0040  
- **Supervisor:** Dr. Ayaluru Murali (Assistant Professor)  
- **Department:** Department of Bioinformatics  
- **Academic Year:** 2024–2026  

---

## 📊 Dataset Information

- **Database:** NCBI Gene Expression Omnibus (GEO)  
- **Accession ID:** GSE226189  
- **Organism:** Homo sapiens  
- **Tissue:** Primary skin fibroblasts  
- **Age Range:** 22–89 years  
- **Platform:** Illumina NovaSeq 6000  
- **Total Samples:** 82  

Raw and processed RNA-seq gene count data were analysed computationally.

---

## 🧪 Analysis Workflow

The following analytical steps were performed:

1. Data acquisition from GEO  
2. Merging individual gene count files  
3. Filtering low-expression genes  
4. Normalisation (log₂ CPM)  
5. Sample stratification (Young vs Aged)  
6. Differential expression analysis  
7. Principal Component Analysis (PCA)  
8. Gene-level visualisation (heatmaps, boxplots)  
9. Functional enrichment analysis (Gene Ontology)  

All analyses were conducted using Python-based bioinformatics scripts.

---



## 📂 Data Availability

Due to GitHub file size limits, large raw and processed gene expression matrices are **not included** in this repository.

- Raw RNA-seq data: Available from GEO (GSE226189)  
- Processed data: Can be regenerated using the provided scripts  
- Data may be shared upon reasonable academic request  

See:
- `data/raw/README.md`
- `data/processed/README.md`

---

## 🛠 Software and Tools

- **Python:** 3.x  
- **Libraries:** NumPy, Pandas, SciPy, Matplotlib, Seaborn, scikit-learn  
- **Functional Enrichment:** g:Profiler  
- **Document Preparation:** LaTeX (Overleaf compatible)  

All analyses were performed in a controlled virtual environment to ensure reproducibility.

---

## 📈 Key Results Summary

- Global transcriptomic differences between young and aged fibroblasts  
- Identification of age-associated genes involved in:
  - Developmental regulation  
  - Extracellular matrix organisation  
  - Signal transduction  
- Functional enrichment highlighted processes related to:
  - Morphogenesis  
  - Multicellular organism development  
  - Vascular development  

---

## 🔁 Reproducibility

All results presented in the thesis can be reproduced by:

1. Downloading raw data from GEO (GSE226189)  
2. Running scripts in the `scripts/` directory sequentially  
3. Regenerating figures and summary tables  

---

## 📜 License

This repository is intended for academic and research use only.  
Reuse of scripts is permitted with proper citation.

---

## 📬 Contact

**Ankur Kumar**  
M.Sc. Bioinformatics  
Department of Bioinformatics  
Pondicherry University  
