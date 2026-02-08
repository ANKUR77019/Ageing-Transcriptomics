import pandas as pd
from gprofiler import GProfiler

genes = [
    "ENSG00000124212",
    "ENSG00000040731"
]

gp = GProfiler(return_dataframe=True)

annot = gp.profile(
    organism="hsapiens",
    query=genes
)

print("Columns returned by g:Profiler:")
print(list(annot.columns))

print("\nPreview:")
print(annot.head())
