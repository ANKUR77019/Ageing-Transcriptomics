import os
import shutil

base_dir = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\raw\GSE226189_RAW"
target_dir = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\raw\gene_counts"

os.makedirs(target_dir, exist_ok=True)

count = 0

for gsm_folder in os.listdir(base_dir):
    gsm_path = os.path.join(base_dir, gsm_folder)

    if not os.path.isdir(gsm_path):
        continue

    for sub in os.listdir(gsm_path):
        if sub.endswith("geneCOUNT"):
            gene_count_dir = os.path.join(gsm_path, sub)

            for f in os.listdir(gene_count_dir):
                src = os.path.join(gene_count_dir, f)

                if os.path.isfile(src):
                    dst = os.path.join(target_dir, gsm_folder + "_" + f)
                    shutil.copy(src, dst)
                    count += 1

print(f"Copied {count} gene count files into gene_counts folder")
