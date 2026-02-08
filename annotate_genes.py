import pandas as pd
from gprofiler import GProfiler

# Load top genes
top_up = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_upregulated_genes.csv"
)
top_down = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_downregulated_genes.csv"
)

genes = list(set(top_up["Gene"].tolist() + top_down["Gene"].tolist()))

gp = GProfiler(return_dataframe=True)

# Use profile instead of convert (more reliable)
annot = gp.profile(
    organism="hsapiens",
    query=genes,
    sources=["GO:BP"]
)

# Extract gene symbol mapping
gene_map = annot[["incoming", "name", "description"]].drop_duplicates()

gene_map.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\gene_annotations_fixed.csv",
    index=False
)

print("Gene annotation completed")
print(gene_map.head())
