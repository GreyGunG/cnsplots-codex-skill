---
name: cnsplots
description: 使用 cnsplots Python 包为科研论文生成 Cell/Nature/Science 期刊级图表。当 Codex 接到"做论文图"、"画发表用的图"、"CNS 风格"、"统计差异图带 p 值"、或具体提到 boxplot/violinplot/heatmap/volcano/survival/forest/ROC/GSEA/UpSet/Sankey/Venn/dotplot/ridgeplot/sankey 等绘图请求时触发。覆盖 25+ 图型 API、调色板（Cell/Nature/Science/Ecotyper/Set1-3/Tableau/parula/BuRd_custom）、统计标注（Mann-Whitney/Welch t/Fisher）、多面板组图、SVG/PDF/PNG 导出与 Adobe Illustrator 兼容。
license: BSD-3-Clause
user-invocable: true
disable-model-invocation: false
---

# cnsplots · 期刊级科研绘图（Codex 版）

`cnsplots` 是 Farid Rashidi 维护的发表级绘图库（[GitHub](https://github.com/faridrashidi/cnsplots) · [Docs](https://cnsplots.farid.one/)），构建在 matplotlib + seaborn 之上，专为 Cell/Nature/Science 投稿的图表细节（字号、刻度、SVG 可编辑性）做优化。

## 工作约定（Codex 必读）

1. **永远先做环境探测**，再写绘图代码。直接 `python3 -c "import cnsplots, sys; print(cnsplots.__version__, sys.executable)"`，失败再决定装（很多 Linux 没有无 3 的 `python`）。
2. **图函数返回 `Axes`**，可继续用 mpl 微调。统一三段式：`cns.figure(...)` → `cns.<plot>(...)` → `cns.savefig(...)`。
3. **像素单位**：`cns.figure(height=150, width=180)` 是像素，期刊单栏≈270px，双栏≈540px。
4. **统计 p 值**：在支持 `pairs` 的函数里传 `pairs=[("A","B"), ...]` 自动出星号；命中默认检验（Mann-Whitney / Welch t / Fisher）。
5. **`heatmapplot` 入参是 `AnnData`**，不是 `DataFrame`。需要时 `import anndata as ad; ad.AnnData(X=...)`。
6. **无图形界面环境**（远程/CI）写 `import matplotlib; matplotlib.use("Agg")`。
7. **`mutool` 缺失只是警告**，不要因此卡住——SVG 仍能产出。

## 安装（按优先级）

```bash
# A. 用户级安装（推荐：系统 Python 全局可用，无需激活）
pip install --user --break-system-packages cnsplots
#   Debian/Ubuntu 屏蔽 --user 时换：
PIP_USER=1 pip install --break-system-packages cnsplots

# B. 项目级 venv（隔离，不污染全局）
uv venv .venv --python 3.12 && uv pip install --python .venv/bin/python cnsplots
#   或：python3 -m venv .venv && .venv/bin/pip install cnsplots

# C. 仓库开发模式
git clone https://github.com/faridrashidi/cnsplots && cd cnsplots && make install

# 可选：让 SVG 在 Adobe Illustrator 中文字仍可编辑
# Linux: apt install mupdf-tools   |   macOS: brew install mupdf-tools

# 撤销：pip uninstall --break-system-packages -y cnsplots
```

依赖较重（含 scanpy / lifelines / gseapy / PyComplexHeatmap，共约 800 MB），首次安装 1–2 分钟。Python ≥ 3.10。

## 顶层 API

| 函数 | 签名 | 说明 |
|---|---|---|
| `cns.figure(height, width, color_cycle=None, color_map=None)` | px | 起新图 |
| `cns.savefig(filepath)` | `.svg`/`.pdf`/`.png` | 导出（svg 优先） |
| `cns.multipanel(max_width, title=None, loc=None)` | 上下文 | 多面板组图 |
| `mp.panel(name, height, width)` / `mp.newline()` | 链式 | 放置面板（标号自动 A/B/C） |
| `cns.add_panel_label("A", pad_left, pad_top)` |  | 手动加标号 |
| `cns.setup_matplotlib(...)` |  | 全局调字号/线宽 |
| `cns.take_legend_out(title=None)` |  | 把图例移出绘图区 |
| `cns.get_hexcolors_from_apalette([0,1], "Set1")` |  | 按索引取色 |
| 颜色常量 | `cns.RED / BLUE / GREEN / ORANGE / PURPLE / VIOLET / PINK / BROWN / GRAY / YELLOW / CHOCOLATE` | hex 字串 |

## 25+ 绘图函数速查

```text
基础统计：boxplot · violinplot · barplot · stripplot · lollipopplot
分布：    histplot · kdeplot · distplot · ridgeplot · qqplot
关系：    scatterplot · regplot · lineplot · slopeplot
矩阵：    heatmapplot(AnnData) · dotplot · confusionplot
科研：    volcanoplot · survivalplot · cumulativeincidenceplot · forestplot · rocplot · gseaplot · phyloplot
集合/比例：stackplot · pieplot · donutplot · vennplot · upsetplot · sankeyplot
```

### 高频函数完整签名（**kwargs 透传 seaborn/matplotlib）

```python
boxplot(data, x, y, pairs=None, showoutliers=False, addcount=False, whis=1.5, **kw)
violinplot(data, x, y, pairs=None, width=0.6, add_box=True, addcount=False, **kw)
barplot(data, x, y, pairs=None, addtip=False, **kw)
stripplot(data, x, y, size=2, showmedian=True, showmeans=False, addcount=False, **kw)
lollipopplot(data, x, y, hue=None, order=None, hue_order=None, pairs=None,
             estimator='mean', errorbar=None, markersize=20, baseline=0, **kw)

scatterplot(data, x, y, s=7, **kw)
regplot(data, x, y, hue=None, s=3, color='black', **kw)
lineplot(**kw)                       # 完全透传
slopeplot(data, x, y, hue)

heatmapplot(adata, layer=None, row_annotation=None, col_annotation=None,
            row_cluster=False, col_cluster=False, row_split=None, col_split=None,
            cmap=None, label='value', xlabel='xlabel', ylabel='ylabel', **kw)
dotplot(data, x, y, color, size, value=None, **kw)
confusionplot(data, x, y, add_pvalue=False, x_order=None, y_order=None,
              positive_x=None, positive_y=None, annot=True, cmap='Blues')

volcanoplot(data, x='log2FoldChange', y='-log10(adjp)', symbol='symbol',
            show_list=None, n_show=10)
survivalplot(data, duration, event, hue, hue_order=None)
forestplot(model, bar_width=None, add_pvalue=True)   # model = cns.CoxModel().fit(...) | LogisticModel().fit(...)
rocplot(data, true_label_col, pred_prob_cols)        # pred_prob_cols 可为 list[str]
gseaplot(data, y, color='NES', cutoff=0.05, cmap='BuRd_custom', top_term=20, size=1.8)

stackplot(data, x, y, bar_order=None, stack_order=None, horizontal=False,
          width=0.5, normalize=True, pairs=None, addcount=False, n_factor=1)
pieplot(data, x, legend='bottom', hue_order=None)
donutplot(data, x, legend='bottom', hue_order=None)
vennplot(lists, labels)              # lists=[set1, set2, set3], labels=("A","B","C")
upsetplot(sets, fig=None, **kw)      # sets={"name": {...}, ...}
sankeyplot(data, x, y, label_rotation=0)
ridgeplot(data, x, y, cmap='viridis')
kdeplot(data, x, add_mode=True, **kw)
qqplot(data, x, **kw)
```

### 调色板（`color_cycle=` 与 `color_map=`）

```text
ColorBrewer 定性： Set1 / Set2 / Set3 / Pastel1 / Pastel2 / Paired / Dark2 / Accent
期刊定性：       Cell / Nature / Science / Tableau / Bold / BlueRed / ECharts
生物专用：       Ecotyper1 .. Ecotyper6
连续/发散 cmap： parula / gnuplot / bwr / hot
                BuRd_custom / WhYlOrRd_custom / OrBu_custom / YlGnBu_custom
```

`cns.palettes("Nature")` 返回颜色列表，可塞进自定义 `palette=` 参数。

### 自动统计标注 → `pairs` 的检验对照

| 函数 | 默认检验 |
|------|---------|
| boxplot / violinplot / stripplot | two-sided Mann-Whitney U |
| barplot / lollipopplot | Welch's t-test |
| stackplot / confusionplot | Fisher's exact |

执行后 stdout 会打印检验来源，可直接抄进 Figure Legend。

## 决策表（用户描述 → 函数）

| 场景 | 选择 |
|------|-----|
| 两/多组数值差异 + p 值 | `boxplot(pairs=...)` 或 `violinplot(pairs=...)` |
| 比例/列联表差异 | `stackplot(normalize=True, pairs=...)` 或 `confusionplot(add_pvalue=True)` |
| 差异表达可视化 | `volcanoplot(show_list=key_genes)` |
| 富集分析 | `dotplot`（颜色+大小双编码） 或 `gseaplot` |
| 生存分析 | `survivalplot(duration, event, hue)` |
| 多变量风险（Cox/Logistic） | `forestplot(cns.CoxModel().fit(df, 'time','event', covariates))` |
| 多模型 AUC 对比 | `rocplot(true_label_col, pred_prob_cols=[...])` |
| 表达矩阵聚类热图 | `heatmapplot(AnnData, row_cluster=True, col_cluster=True)` |
| 集合交集 ≤3 / >3 | `vennplot` / `upsetplot` |
| 流向 / 配对前后变化 | `sankeyplot` / `slopeplot` |
| 单细胞子群占比 | `stackplot` + `Ecotyper1..6` 调色板 |

## 多面板组图骨架

```python
mp = cns.multipanel(max_width=540, title="Figure 1")

mp.panel("A", height=160, width=170)
cns.boxplot(data=df, x="group", y="expr", pairs=[("WT","KO")])

mp.panel("B", height=160, width=170)
cns.volcanoplot(data=deg, n_show=8)

mp.newline()
mp.panel("C", height=160, width=350)
cns.heatmapplot(adata=ad, row_cluster=True, col_annotation=["subtype"])

cns.savefig("Figure1.svg")
```

## Recipes（位于 `recipes/`，cp 后改列名即可跑）

| 文件 | 演示 |
|------|------|
| `recipes/01_boxplot_with_stats.py` | 分组箱线图 + Mann-Whitney p 值 |
| `recipes/02_volcano.py` | 火山图 + 关键基因标注 |
| `recipes/03_survival_km.py` | Kaplan-Meier 生存曲线 |
| `recipes/04_heatmap_anndata.py` | AnnData 表达矩阵聚类热图 |
| `recipes/05_multipanel_figure1.py` | 论文 Figure 1 三联面板 |
| `recipes/06_roc_multimodel.py` | 多模型 ROC 对比 |
| `recipes/07_dotplot_enrichment.py` | GO/KEGG 富集点图 |
| `recipes/08_upset_sets.py` | UpSet 多集合交集 |

## 常见坑位

| 现象 | 处理 |
|------|------|
| `RuntimeWarning: MuPDF's mutool is unavailable` | 非致命；要 Illustrator 完整可编辑 SVG → 装 `mupdf-tools` |
| 图像比预期小一倍 | 像素不是英寸；单栏 ≈270，双栏 ≈540 |
| `heatmapplot` 报 `AnnData expected` | `import anndata as ad; ad.AnnData(X=df.values, obs=..., var=...)` |
| `pairs` 标的 p 值不出现 | 元组里的标签必须出现在 x 列里；否则静默忽略 |
| 中文方块 | `cns.apply_unicode_font("Noto Sans CJK SC")` 或自行设 `font.sans-serif` |
| 图例挡图 | `cns.take_legend_out()` 后再 `savefig` |
| Volcano 无 symbol | 数据需要 `symbol` / `log2FoldChange` / `-log10(adjp)` 三列（或显式传列名参数） |
| 安装因 PEP 668 失败 | 走 `uv venv` 或 `python -m venv` 隔离 |

## 引用

```bibtex
@software{cnsplots,
  author = {Rashidi, Farid},
  title  = {cnsplots: Publication-Ready Scientific Plots},
  year   = {2026},
  url    = {https://github.com/faridrashidi/cnsplots}
}
```

License: BSD-3-Clause。源码：<https://github.com/faridrashidi/cnsplots> · 文档：<https://cnsplots.farid.one/>
