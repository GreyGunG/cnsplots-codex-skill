# cnsplots Codex 技能

这是一个给 Codex 使用的 `cnsplots` 绘图技能，用来生成投稿级科研图。它基于
[`cnsplots`](https://github.com/faridrashidi/cnsplots) 这个 matplotlib/seaborn
生态的绘图库，重点面向 Cell、Nature、Science 风格的论文图。

这个技能会帮助 Codex 在画图前检查 Python 环境，选择合适的 `cnsplots` API，编写可复现的绘图脚本，
添加统计标注，并导出可编辑的 SVG/PDF/PNG 文件，方便直接用于论文、汇报和补充材料。

## 适用场景

- 箱线图、小提琴图、柱状图、散点图、回归图、折线图、棒棒糖图和山峦图
- 火山图、生存曲线、森林图、ROC 曲线、GSEA 图、富集点图、热图和混淆矩阵
- Venn 图、UpSet 图、Sankey 图、堆叠比例图、饼图和环形图
- Cell/Nature/Science 风格配色和论文版面尺寸
- 通过 `pairs=` 自动添加 p 值和显著性星号
- 组装适合论文 Figure 1 的多面板组合图
- 在无图形界面的服务器或 CI 环境中使用 matplotlib `Agg` 后端出图

## 安装方式

把这个仓库复制到 Codex 的 skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/GreyGunG/cnsplots-codex-skill.git ~/.codex/skills/cnsplots
```

然后在 Codex 里这样调用：

```text
$cnsplots 用我的 CSV 画一张 Nature 风格箱线图，带 WT vs KO 的 p 值，导出 SVG。
```

## Python 依赖

这个技能需要当前 Python 环境已经安装 `cnsplots` 包。Codex 会先执行下面的命令检查环境：

```bash
python3 -c "import cnsplots, sys; print(cnsplots.__version__, sys.executable)"
```

如果没有安装，可以用用户级安装：

```bash
pip install --user --break-system-packages cnsplots
```

也可以在项目里创建隔离环境：

```bash
python3 -m venv .venv
.venv/bin/pip install cnsplots
```

## 内置示例

`recipes/` 目录里放了常见图型的起步脚本：

- `01_boxplot_with_stats.py`：带统计标注的分组箱线图
- `02_volcano.py`：差异分析火山图
- `03_survival_km.py`：Kaplan-Meier 生存曲线
- `04_heatmap_anndata.py`：基于 AnnData 的表达矩阵热图
- `05_multipanel_figure1.py`：论文 Figure 1 多面板组合图
- `06_roc_multimodel.py`：多模型 ROC 曲线对比
- `07_dotplot_enrichment.py`：GO/KEGG 富集点图
- `08_upset_sets.py`：多集合交集 UpSet 图

## 引用与来源

本仓库只是把 `cnsplots` 的使用方式封装成 Codex skill。绘图库本体由 Farid Rashidi 维护：

- 源码：<https://github.com/faridrashidi/cnsplots>
- 文档：<https://cnsplots.farid.one/>

建议引用：

```bibtex
@software{cnsplots,
  author = {Rashidi, Farid},
  title  = {cnsplots: Publication-Ready Scientific Plots},
  year   = {2026},
  url    = {https://github.com/faridrashidi/cnsplots}
}
```
