import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CHANGE THIS to your top gene
GENE_ID = "ENSG00000124212"

# Load normalized expression data
expr = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\normalized_log2CPM_young_vs_aged.csv",
    index_col=0
)

# Load metadata
meta = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\sample_metadata.csv"
)
meta = meta[meta["Group"].isin(["Young", "Aged"])]

# Extract gene expression
gene_expr = expr.loc[GENE_ID]

# Combine into one DataFrame
plot_df = pd.DataFrame({
    "Expression": gene_expr.values,
    "Group": meta["Group"].values
})

# Plot
plt.figure()
sns.boxplot(x="Group", y="Expression", data=plot_df)
sns.stripplot(x="Group", y="Expression", data=plot_df, color="black", alpha=0.5)

plt.title(f"Expression of {GENE_ID} in Young vs Aged Samples")
plt.ylabel("log2(CPM + 1)")
plt.xlabel("")
plt.show()
