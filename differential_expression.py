import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Load normalized data
expr = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\normalized_log2CPM_young_vs_aged.csv",
    index_col=0
)

meta = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\sample_metadata.csv"
)

# Keep only Young and Aged
meta = meta[meta["Group"].isin(["Young", "Aged"])]

young_samples = meta[meta["Group"] == "Young"]["Sample"]
aged_samples = meta[meta["Group"] == "Aged"]["Sample"]

results = []

for gene in expr.index:
    y_vals = expr.loc[gene, young_samples]
    a_vals = expr.loc[gene, aged_samples]

    # log2 fold change (Aged - Young)
    log2fc = a_vals.mean() - y_vals.mean()

    # t-test
    t_stat, p_val = ttest_ind(a_vals, y_vals, equal_var=False)

    results.append([gene, log2fc, p_val])

deg_df = pd.DataFrame(
    results,
    columns=["Gene", "log2FC", "p_value"]
)

# Multiple testing correction (FDR - Benjamini-Hochberg)
deg_df["rank"] = deg_df["p_value"].rank(method="first")
deg_df["FDR"] = deg_df["p_value"] * len(deg_df) / deg_df["rank"]
deg_df["FDR"] = deg_df["FDR"].clip(upper=1.0)

# Save results
deg_df.sort_values("p_value", inplace=True)
deg_df.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\differential_expression_results.csv",
    index=False
)

print("Differential expression analysis complete")
print(deg_df.head())
