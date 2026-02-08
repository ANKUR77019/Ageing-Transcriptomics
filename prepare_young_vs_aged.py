import pandas as pd

# Load data
expr = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\cleaned_expression_matrix.csv",
    index_col=0
)

meta = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\sample_metadata.csv"
)

# Keep only Young and Aged samples
meta_ya = meta[meta["Group"].isin(["Young", "Aged"])]

# Subset expression matrix
expr_ya = expr[meta_ya["Sample"]]

print("Expression shape (Young vs Aged):", expr_ya.shape)

# Filter low-expression genes
# Keep genes with at least 10 counts in ≥20% of samples
min_samples = int(0.2 * expr_ya.shape[1])
filtered_expr = expr_ya[(expr_ya >= 10).sum(axis=1) >= min_samples]

print("After filtering low-expression genes:", filtered_expr.shape)

# Save filtered matrix
filtered_expr.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\filtered_expression_young_vs_aged.csv"
)

print("Filtered Young vs Aged matrix saved")
