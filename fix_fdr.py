import pandas as pd
import statsmodels.stats.multitest as smm

# Load DE results
deg = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\differential_expression_results.csv"
)

# Correct p-values using Benjamini-Hochberg
deg["FDR"] = smm.multipletests(deg["p_value"], method="fdr_bh")[1]

# Save corrected results
deg.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\differential_expression_results_FDR.csv",
    index=False
)

print("FDR correction updated")
print(deg.sort_values("FDR").head())
