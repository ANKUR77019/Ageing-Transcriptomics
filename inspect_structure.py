import os

base_dir = r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\raw\GSE226189_RAW"

shown = 0

for root, dirs, files in os.walk(base_dir):
    if dirs:
        print("\nDIR PATH:", root)
        for d in dirs:
            print("  └──", d)
            shown += 1
            if shown > 20:
                print("\n--- stopping after 20 directories ---")
                exit()

    if files:
        print("\nFILE PATH:", root)
        for f in files:
            print("  └──", f)
            shown += 1
            if shown > 20:
                print("\n--- stopping after 20 files ---")
                exit()
