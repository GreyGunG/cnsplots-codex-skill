"""
Recipe 02 — 火山图（差异表达分析）。
输入需要包含三列：log2FoldChange / -log10(adjp) / symbol。
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import cnsplots as cns

rng = np.random.default_rng(42)
n = 800
deg = pd.DataFrame({
    "symbol":         [f"GENE{i}" for i in range(n)],
    "log2FoldChange": rng.normal(0, 1.5, n),
    "-log10(adjp)":   rng.gamma(2, 1.5, n),
})
key_genes = ["GENE3", "GENE17", "GENE42", "GENE88", "GENE150"]

cns.figure(height=180, width=200, color_cycle="Cell")
cns.volcanoplot(
    data=deg,
    x="log2FoldChange",
    y="-log10(adjp)",
    symbol="symbol",
    show_list=key_genes,    # 强制标注的基因
    n_show=10,              # 在剩余基因中再标注 top10
)
cns.savefig("volcano.svg")
