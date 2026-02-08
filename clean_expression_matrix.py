import pandas as pd

input_file = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\merged_gene_expression_matrix.csv"

# Read file
df = pd.read_csv(input_file)

# Drop the Tracking_ID row
df = df[df["Gene"] != "Tracking_ID"]

# Set Gene column as index
df.set_index("Gene", inplace=True)

# Convert all values to numeric
df = df.apply(pd.to_numeric)

print("Cleaned matrix shape:", df.shape)
print(df.head())

# Save cleaned matrix
output_file = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\cleaned_expression_matrix.csv"
df.to_csv(output_file)

print("Saved cleaned expression matrix")
