"""
Recipe 03 — Kaplan-Meier 生存曲线 + log-rank。
"""
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import cnsplots as cns

rng = np.random.default_rng(0)
n = 200
df = pd.DataFrame({
    "time":  rng.exponential(20, n).clip(0, 60),
    "event": rng.binomial(1, 0.7, n),
    "arm":   rng.choice(["Treatment", "Control"], n),
})

cns.figure(height=160, width=180, color_cycle="Science")
cns.survivalplot(
    data=df,
    duration="time",
    event="event",
    hue="arm",
    hue_order=["Control", "Treatment"],
)
cns.savefig("survival_km.svg")
