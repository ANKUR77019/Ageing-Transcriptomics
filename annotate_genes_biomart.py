import pandas as pd
from pybiomart import Dataset

# Load your genes
top_up = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_upregulated_genes.csv"
)
top_down = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_downregulated_genes.csv"
)

genes = list(set(top_up["Gene"].tolist() + top_down["Gene"].tolist()))

# Connect to Ensembl BioMart
dataset = Dataset(name='hsapiens_gene_ensembl', host='http://www.ensembl.org')

# Query annotation
annot = dataset.query(
    attributes=['ensembl_gene_id', 'external_gene_name', 'description'],
    filters={'ensembl_gene_id': genes}
)

annot.columns = ['ENSG_ID', 'Gene_Symbol', 'Description']

annot.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\gene_annotations_biomart.csv",
    index=False
)

print("Gene annotation via BioMart completed")
print(annot.head())
