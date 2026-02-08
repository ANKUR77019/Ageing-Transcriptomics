import pandas as pd
import numpy as np

# Load filtered data
expr = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\filtered_expression_young_vs_aged.csv",
    index_col=0
)

# Calculate Counts Per Million (CPM)
library_sizes = expr.sum(axis=0)
cpm = expr.div(library_sizes, axis=1) * 1e6

# Log2 transform
log2_cpm = np.log2(cpm + 1)

print("Normalized matrix shape:", log2_cpm.shape)
print(log2_cpm.head())

# Save normalized data
log2_cpm.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\normalized_log2CPM_young_vs_aged.csv"
)

print("Normalized expression matrix saved")
