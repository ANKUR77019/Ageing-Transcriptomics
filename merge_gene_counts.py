import pandas as pd
import os

data_dir = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\raw\GSE226189_RAW"

all_items = os.listdir(data_dir)

# Select files that contain 'geneCOUNT' and are real files
files = [
    f for f in all_items
    if "geneCOUNT" in f and os.path.isfile(os.path.join(data_dir, f))
]

print("All items in directory:", len(all_items))
print("geneCOUNT-like files found:", len(files))

if len(files) == 0:
    raise RuntimeError("No readable geneCOUNT files found. Check file extensions and OneDrive sync.")

merged_df = None

for file in files:
    file_path = os.path.join(data_dir, file)

    try:
        df = pd.read_csv(file_path, sep="\t", header=None)
    except Exception as e:
        print(f"Skipping {file}: {e}")
        continue

    # Keep first two columns only
    df = df.iloc[:, :2]
    df.columns = ["Gene", file.replace(".txt", "").replace("_geneCOUNT", "")]

    if merged_df is None:
        merged_df = df
    else:
        merged_df = pd.merge(merged_df, df, on="Gene", how="inner")

if merged_df is None:
    raise RuntimeError("All geneCOUNT files failed to load.")

merged_df.set_index("Gene", inplace=True)

print("Merged matrix created successfully")
print("Genes:", merged_df.shape[0])
print("Samples:", merged_df.shape[1])

output_path = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\merged_gene_expression_matrix.csv"
merged_df.to_csv(output_path)

print("Saved merged matrix to:", output_path)
