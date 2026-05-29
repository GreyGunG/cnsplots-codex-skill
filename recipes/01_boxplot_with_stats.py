"""
Recipe 01 — 分组箱线图 + 统计显著性标注（Mann-Whitney U）。
跑法：python 01_boxplot_with_stats.py
输出：boxplot_stats.svg
"""
import matplotlib
matplotlib.use("Agg")

import cnsplots as cns
import seaborn as sns

df = sns.load_dataset("tips")

cns.figure(height=160, width=180, color_cycle="Nature")
cns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    pairs=[("Thur", "Fri"), ("Sat", "Sun"), ("Thur", "Sun")],
    showoutliers=False,
    addcount=True,            # 在 x 轴下方标注每组样本数
    whis=1.5,
)
cns.savefig("boxplot_stats.svg")
