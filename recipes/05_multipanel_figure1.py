"""
Recipe 05 — 完整论文 Figure 1 组图（multipanel）。
展示：箱线图 + 火山图 + 生存曲线 三联面板。
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import seaborn as sns
import cnsplots as cns

rng = np.random.default_rng(1)

# --- 数据 ---
df_box  = sns.load_dataset("tips")
deg     = pd.DataFrame({
    "symbol":         [f"GENE{i}" for i in range(400)],
    "log2FoldChange": rng.normal(0, 1.5, 400),
    "-log10(adjp)":   rng.gamma(2, 1.5, 400),
})
df_surv = pd.DataFrame({
    "time":  rng.exponential(20, 200).clip(0, 60),
    "event": rng.binomial(1, 0.7, 200),
    "arm":   rng.choice(["Treatment", "Control"], 200),
})

# --- 组图 ---
mp = cns.multipanel(max_width=540, title="Figure 1")

mp.panel("A", height=160, width=170)
cns.boxplot(data=df_box, x="day", y="total_bill",
            pairs=[("Thur", "Sun"), ("Fri", "Sat")])

mp.panel("B", height=160, width=170)
cns.volcanoplot(data=deg, n_show=6)

mp.panel("C", height=160, width=170)
cns.survivalplot(data=df_surv, duration="time", event="event", hue="arm")

cns.savefig("Figure1.svg")
