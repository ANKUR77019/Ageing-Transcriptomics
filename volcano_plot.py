import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load corrected DE results
deg = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\differential_expression_results_FDR.csv"
)

# Define significance
deg["Significant"] = (deg["FDR"] < 0.05) & (abs(deg["log2FC"]) > 1)

plt.figure()
plt.scatter(
    deg["log2FC"],
    -np.log10(deg["p_value"]),
    alpha=0.5
)

# Highlight significant genes
sig = deg[deg["Significant"]]
plt.scatter(
    sig["log2FC"],
    -np.log10(sig["p_value"])
)

plt.axvline(1)
plt.axvline(-1)
plt.axhline(-np.log10(0.05))

plt.xlabel("log2 Fold Change (Aged vs Young)")
plt.ylabel("-log10(p-value)")
plt.title("Volcano Plot of Age-Associated Genes")

plt.show()
