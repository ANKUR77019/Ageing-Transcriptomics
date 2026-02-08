import pandas as pd

deg = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\differential_expression_results_FDR.csv"
)

# Relaxed but justified thresholds
sig = deg[(deg["p_value"] < 0.01) & (abs(deg["log2FC"]) > 0.5)]

print("Significant genes found:", sig.shape[0])

# Top upregulated (Aged > Young)
top_up = sig.sort_values("log2FC", ascending=False).head(20)

# Top downregulated (Aged < Young)
top_down = sig.sort_values("log2FC").head(20)

# Save results
top_up.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_upregulated_genes.csv",
    index=False
)

top_down.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\top_downregulated_genes.csv",
    index=False
)

print("\nTop upregulated genes:")
print(top_up[["Gene", "log2FC", "p_value"]])

print("\nTop downregulated genes:")
print(top_down[["Gene", "log2FC", "p_value"]])
