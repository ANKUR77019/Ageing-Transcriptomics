import pandas as pd
from pybiomart import Dataset

# Load genes
top_up = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_upregulated_genes.csv"
)
top_down = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_downregulated_genes.csv"
)

genes = list(set(top_up["Gene"].tolist() + top_down["Gene"].tolist()))

dataset = Dataset(
    name="hsapiens_gene_ensembl",
    host="http://www.ensembl.org"
)

# Query ALL genes, then filter locally (robust & safe for small lists)
annot = dataset.query(
    attributes=[
        "ensembl_gene_id",
        "external_gene_name",
        "description"
    ]
)

annot.columns = ["ENSG_ID", "Gene_Symbol", "Description"]

annot = annot[annot["ENSG_ID"].isin(genes)]

annot.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\gene_annotations_biomart.csv",
    index=False
)

print("BioMart annotation completed successfully")
print(annot.head())
