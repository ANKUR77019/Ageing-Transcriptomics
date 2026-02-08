import os

base_dir = r"C:\Users\Dell\Documents\Djangoproject\myproject1\data\raw\GSE226189_RAW"

print("Exists:", os.path.exists(base_dir))
print("Contents:", os.listdir(base_dir))
