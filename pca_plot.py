import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load normalized data
expr = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\normalized_log2CPM_young_vs_aged.csv",
    index_col=0
)

# Transpose: samples × genes
X = expr.T

# Run PCA
pca = PCA(n_components=2)
pcs = pca.fit_transform(X)

# Load metadata
meta = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\sample_metadata.csv"
)
meta = meta[meta["Group"].isin(["Young", "Aged"])]

# Plot
plt.figure()
for group in ["Young", "Aged"]:
    idx = meta["Group"] == group
    plt.scatter(pcs[idx, 0], pcs[idx, 1], label=group)

plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
plt.title("PCA of Gene Expression (Young vs Aged)")
plt.legend()
plt.show()
