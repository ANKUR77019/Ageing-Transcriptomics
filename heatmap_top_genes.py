import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load normalized expression matrix
expr = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\normalized_log2CPM_young_vs_aged.csv",
    index_col=0
)

# Load DE results
deg = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\differential_expression_results_FDR.csv"
)

# Use relaxed, justified thresholds
sig = deg[(deg["p_value"] < 0.01) & (abs(deg["log2FC"]) > 0.5)]

# Select top genes
top_up = sig.sort_values("log2FC", ascending=False).head(15)
top_down = sig.sort_values("log2FC").head(15)

top_genes = pd.concat([top_up, top_down])["Gene"]

# Subset expression data
heatmap_data = expr.loc[top_genes]

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(
    heatmap_data,
    cmap="viridis",
    yticklabels=True
)

plt.title("Heatmap of Top Age-Associated Genes (Young vs Aged)")
plt.xlabel("Samples")
plt.ylabel("Genes")
plt.tight_layout()
plt.show()
