import pandas as pd
import matplotlib.pyplot as plt

# Load enrichment results
enrich = pd.read_csv(
    r"C:\Users\Dell\OneDrive\Desktop\Anti ageing dissertation\data\processed\functional_enrichment_results.csv"
)

# Keep GO Biological Process only
bp = enrich[enrich["source"] == "GO:BP"].head(10)

plt.figure()
plt.barh(bp["name"], -bp["p_value"].apply(lambda x: -x))
plt.xlabel("-log10(p-value)")
plt.title("Top Enriched Biological Processes")
plt.tight_layout()
plt.show()
