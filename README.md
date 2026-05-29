# cnsplots Codex Skill

这是一个给 Codex 用的绘图 skill。你把数据、列名和想要的图型告诉 Codex，它会按
`cnsplots` 的写法帮你生成脚本，最后导出适合论文和汇报使用的 SVG、PDF 或 PNG。

`cnsplots` 本身是 Farid Rashidi 维护的 Python 绘图库，基于 matplotlib 和 seaborn，
主要用来做 Cell、Nature、Science 这类期刊风格的科研图。本仓库只是把它整理成 Codex
可直接调用的 skill，不是 `cnsplots` 的源码仓库。

## 适合拿来做什么

常见论文图基本都可以从这里起步：

- 组间比较：箱线图、小提琴图、柱状图、散点图、棒棒糖图
- 组学分析：火山图、富集点图、GSEA 图、热图
- 临床和模型评估：生存曲线、森林图、ROC 曲线、混淆矩阵
- 集合和比例：Venn 图、UpSet 图、堆叠比例图、Sankey 图、饼图、环形图
- 论文排版：多面板 Figure、期刊配色、可编辑 SVG 导出

如果图型支持 `pairs=`，Codex 会优先用 `cnsplots` 自带的统计标注来加 p 值和显著性星号。

## 安装

把这个仓库放到 Codex 的 skills 目录下：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/GreyGunG/cnsplots-codex-skill.git ~/.codex/skills/cnsplots
```

之后在 Codex 里直接点名使用：

```text
$cnsplots 用 data.csv 画一张 Nature 风格箱线图，x 是 group，y 是 score，比较 Control 和 Treatment，导出 SVG。
```

## Python 环境

这个 skill 只负责告诉 Codex 怎么用 `cnsplots`；真正画图还需要本机 Python 能导入
`cnsplots` 包。

Codex 会先检查环境：

```bash
python3 -c "import cnsplots, sys; print(cnsplots.__version__, sys.executable)"
```

没装的话，可以装到当前用户环境：

```bash
pip install --user --break-system-packages cnsplots
```

更推荐在项目里单独建一个虚拟环境：

```bash
python3 -m venv .venv
.venv/bin/pip install cnsplots
```

`cnsplots` 的依赖比较多，第一次安装会花一点时间。

## 自带示例

`recipes/` 里放了一组可以直接改列名复用的脚本：

- `01_boxplot_with_stats.py`：分组箱线图，带统计标注
- `02_volcano.py`：差异分析火山图
- `03_survival_km.py`：Kaplan-Meier 生存曲线
- `04_heatmap_anndata.py`：AnnData 表达矩阵热图
- `05_multipanel_figure1.py`：三联面板 Figure 1
- `06_roc_multimodel.py`：多模型 ROC 对比
- `07_dotplot_enrichment.py`：GO/KEGG 富集点图
- `08_upset_sets.py`：多集合 UpSet 图

## 常用提示词

```text
$cnsplots 根据 metadata.csv 画一张分组小提琴图，x=group，y=expression，比较 A 和 B，导出 PDF。
```

```text
$cnsplots 用 deg.csv 画火山图，log2FC 列是 log2FoldChange，校正 p 值列是 padj，标出 TP53、KRAS、MYC。
```

```text
$cnsplots 把这三个图合成一个 Figure 1，多面板排版，宽度按双栏处理，导出可编辑 SVG。
```

## 来源

`cnsplots` 项目地址：

- GitHub：<https://github.com/faridrashidi/cnsplots>
- 文档：<https://cnsplots.farid.one/>

如果论文里用到了 `cnsplots`，建议引用原项目：

```bibtex
@software{cnsplots,
  author = {Rashidi, Farid},
  title  = {cnsplots: Publication-Ready Scientific Plots},
  year   = {2026},
  url    = {https://github.com/faridrashidi/cnsplots}
}
```
