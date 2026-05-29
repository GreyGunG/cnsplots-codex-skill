"""
Recipe 07 — 富集分析 dotplot（颜色编码 NES、点大小编码基因数）。
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import cnsplots as cns

rng = np.random.default_rng(3)
groups   = ["GroupA", "GroupB", "GroupC"]
pathways = [f"Pathway_{i}" for i in range(8)]
records  = []
for g in groups:
    for p in pathways:
        records.append({
            "group":   g,
            "pathway": p,
            "NES":     rng.normal(0, 1.2),
            "n_genes": rng.integers(5, 80),
        })
df = pd.DataFrame(records)

cns.figure(height=200, width=240, color_map="BuRd_custom")
cns.dotplot(
    data=df,
    x="group",
    y="pathway",
    color="NES",      # 点的颜色
    size="n_genes",   # 点的大小
)
cns.savefig("dotplot_enrichment.svg")
