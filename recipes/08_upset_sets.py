"""
Recipe 08 — UpSet 多集合交集（>3 集合首选 UpSet 而非 Venn）。
"""
import matplotlib
matplotlib.use("Agg")

import cnsplots as cns

sets = {
    "DEG_TumorVsNormal": {"GENE1", "GENE2", "GENE3", "GENE4", "GENE5", "GENE6"},
    "DEG_StageIIIvsI":   {"GENE2", "GENE3", "GENE7", "GENE8"},
    "Druggable":         {"GENE1", "GENE3", "GENE9", "GENE10"},
    "Hypoxia_signature": {"GENE3", "GENE5", "GENE7", "GENE11"},
}

cns.figure(height=200, width=260)
cns.upsetplot(sets=sets)
cns.savefig("upset_sets.svg")
