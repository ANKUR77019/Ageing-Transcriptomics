import pandas as pd
from gprofiler import GProfiler

# Load differential expression results
deg = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\differential_expression_results_FDR.csv"
)

# Use relaxed, justified thresholds
sig_genes = deg[
    (deg["p_value"] < 0.01) & (abs(deg["log2FC"]) > 0.5)
]["Gene"].tolist()

print("Number of genes for enrichment:", len(sig_genes))

# Initialize g:Profiler
gp = GProfiler(return_dataframe=True)

# Run enrichment
results = gp.profile(
    organism="hsapiens",
    query=sig_genes
)

# Save results
results.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\functional_enrichment_results.csv",
    index=False
)

print("Top enriched terms:")
print(results[["source", "name", "p_value"]].head(10))
