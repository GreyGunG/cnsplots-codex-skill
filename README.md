# cnsplots Codex Skill

Codex skill for generating publication-ready scientific figures with
[`cnsplots`](https://github.com/faridrashidi/cnsplots), a matplotlib/seaborn-based
plotting library tuned for Cell, Nature, and Science style figures.

This skill helps Codex choose the right `cnsplots` API, check the Python
environment before plotting, write reproducible figure scripts, add statistical
annotations, and export editable SVG/PDF/PNG figures for papers and reports.

## What It Covers

- Box, violin, bar, strip, lollipop, scatter, regression, line, and ridge plots
- Volcano, survival, forest, ROC, GSEA, dot, heatmap, and confusion plots
- Venn, UpSet, Sankey, stack, pie, and donut plots
- Cell/Nature/Science-style palettes and figure sizing
- Automatic p-value annotations through supported `pairs=` arguments
- Multi-panel figure assembly for manuscript-style Figure 1 layouts
- Headless server/CI plotting with matplotlib `Agg`

## Install

Copy this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/GreyGunG/cnsplots-codex-skill.git ~/.codex/skills/cnsplots
```

Then invoke it in Codex:

```text
$cnsplots 用我的 CSV 画一张 Nature 风格箱线图，带 WT vs KO 的 p 值，导出 SVG。
```

## Python Dependency

The skill expects the Python package `cnsplots` to be available. Codex will check
first with:

```bash
python3 -c "import cnsplots, sys; print(cnsplots.__version__, sys.executable)"
```

If missing, install it with one of:

```bash
pip install --user --break-system-packages cnsplots
```

or in an isolated project environment:

```bash
python3 -m venv .venv
.venv/bin/pip install cnsplots
```

## Included Recipes

The `recipes/` folder contains small starting points for common figure types:

- `01_boxplot_with_stats.py`
- `02_volcano.py`
- `03_survival_km.py`
- `04_heatmap_anndata.py`
- `05_multipanel_figure1.py`
- `06_roc_multimodel.py`
- `07_dotplot_enrichment.py`
- `08_upset_sets.py`

## Attribution

This repository packages a Codex skill for working with `cnsplots`. The plotting
library itself is maintained by Farid Rashidi:

- Source: <https://github.com/faridrashidi/cnsplots>
- Docs: <https://cnsplots.farid.one/>

Suggested citation:

```bibtex
@software{cnsplots,
  author = {Rashidi, Farid},
  title  = {cnsplots: Publication-Ready Scientific Plots},
  year   = {2026},
  url    = {https://github.com/faridrashidi/cnsplots}
}
```
