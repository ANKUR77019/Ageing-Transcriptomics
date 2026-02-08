import pandas as pd
import re

# Load cleaned expression matrix
expr_file = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\cleaned_expression_matrix.csv"
df = pd.read_csv(expr_file, index_col=0)

# Extract sample names
samples = df.columns

metadata = []

for s in samples:
    # Extract AGE number using regex
    match = re.search(r'AGE(\d+)', s)
    age = int(match.group(1)) if match else None

    if age is not None:
        if age <= 40:
            group = "Young"
        elif age >= 65:
            group = "Aged"
        else:
            group = "Middle"
    else:
        group = None

    metadata.append({
        "Sample": s,
        "Age": age,
        "Group": group
    })

meta_df = pd.DataFrame(metadata)

print(meta_df["Group"].value_counts())
print(meta_df.head())

# Save metadata
meta_df.to_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\sample_metadata.csv",
    index=False
)

print("Sample metadata saved")
