"""
Recipe 04 — AnnData 表达矩阵热图（双向聚类 + 行/列注释）。
注意：heatmapplot 的入参是 AnnData，不是 DataFrame。
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import anndata as ad
import cnsplots as cns

rng = np.random.default_rng(7)
n_obs, n_var = 60, 30
X = rng.normal(0, 1, (n_obs, n_var))
X[:30] += 1.5  # 让前 30 个样本表达更高

obs = pd.DataFrame({
    "subtype": np.repeat(["A", "B"], n_obs // 2),
    "stage":   np.tile(["I", "II", "III"], n_obs // 3),
}, index=[f"S{i}" for i in range(n_obs)])
var = pd.DataFrame({
    "module": np.tile(["M1", "M2", "M3"], n_var // 3),
}, index=[f"G{i}" for i in range(n_var)])

adata = ad.AnnData(X=X, obs=obs, var=var)

cns.figure(height=260, width=280, color_map="BuRd_custom")
cns.heatmapplot(
    adata=adata,
    row_annotation=["subtype", "stage"],
    col_annotation=["module"],
    row_cluster=True,
    col_cluster=True,
    row_split="subtype",
    cmap="BuRd_custom",
    label="expr (z)",
)
cns.savefig("heatmap_anndata.svg")
