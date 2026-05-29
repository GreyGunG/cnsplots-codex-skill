"""
Recipe 06 — 多模型 ROC 曲线对比。
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import cnsplots as cns

rng = np.random.default_rng(2)
n = 400
true_y = rng.binomial(1, 0.4, n)
df = pd.DataFrame({
    "label":          true_y,
    "RandomForest":   np.clip(true_y * 0.7 + rng.normal(0.3, 0.2, n), 0, 1),
    "LogisticReg":    np.clip(true_y * 0.5 + rng.normal(0.4, 0.25, n), 0, 1),
    "XGBoost":        np.clip(true_y * 0.8 + rng.normal(0.2, 0.15, n), 0, 1),
})

cns.figure(height=180, width=180, color_cycle="Tableau")
cns.rocplot(
    data=df,
    true_label_col="label",
    pred_prob_cols=["RandomForest", "LogisticReg", "XGBoost"],
)
cns.savefig("roc_multimodel.svg")
