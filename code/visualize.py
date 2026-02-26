#!/usr/bin/env python3
"""
Generate visualizations for the Search Intent & Query Analysis Experiment.
Outputs: 4 PNG chart images in the ../charts/ directory.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import re
from collections import Counter
import os

matplotlib.use("Agg")
plt.rcParams.update({
    "figure.dpi": 150,
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.labelsize": 12,
})

os.makedirs("../charts", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("../data/Cleaned_Dataset.csv")
total = len(df)

# ── Color palette ──
COLORS = {
    "Informational": "#4A90D9",
    "Transactional": "#E8734A",
    "Comparative":   "#F5C242",
    "Navigational":  "#6CC24A",
}
ACCENT = "#2C3E50"
BG_COLOR = "#FAFBFC"

# ==========================================================================
# Chart 1: Intent Distribution — Pie Chart
# ==========================================================================
print("📊 Generating: Intent Distribution Pie Chart...")

intent_counts = df["Intent_Category"].value_counts()
labels = intent_counts.index.tolist()
sizes = intent_counts.values.tolist()
colors = [COLORS.get(l, "#999") for l in labels]
explode = [0.05 if l == "Informational" else 0 for l in labels]

fig, ax = plt.subplots(figsize=(8, 6), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct=lambda p: f'{p:.1f}%\n({int(p*total/100)})',
    colors=colors, explode=explode, startangle=140,
    textprops={"fontsize": 11, "fontweight": "bold"},
    pctdistance=0.72, labeldistance=1.12,
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)
for t in autotexts:
    t.set_fontsize(9)
    t.set_color("white")
    t.set_fontweight("bold")

ax.set_title("Search Intent Distribution", fontsize=16, fontweight="bold",
             color=ACCENT, pad=20)
fig.text(0.5, 0.02, f"Total Queries: {total}", ha="center", fontsize=10,
         color="#666", style="italic")

plt.tight_layout()
plt.savefig("../charts/01_intent_distribution_pie.png", bbox_inches="tight",
            facecolor=BG_COLOR)
plt.close()
print("  ✅ ../charts/01_intent_distribution_pie.png")

# ==========================================================================
# Chart 2: Intent Distribution — Bar Chart
# ==========================================================================
print("📊 Generating: Intent Distribution Bar Chart...")

fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

bars = ax.barh(labels[::-1], [intent_counts[l] for l in labels[::-1]],
               color=[COLORS.get(l, "#999") for l in labels[::-1]],
               edgecolor="white", linewidth=1.5, height=0.6)

for bar, label in zip(bars, labels[::-1]):
    count = intent_counts[label]
    pct = count / total * 100
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f"{count}  ({pct:.1f}%)", va="center", fontsize=11,
            fontweight="bold", color=ACCENT)

ax.set_xlabel("Number of Queries", fontsize=12, color=ACCENT)
ax.set_title("Search Intent Category Distribution", fontsize=16,
             fontweight="bold", color=ACCENT, pad=15)
ax.set_xlim(0, max(sizes) * 1.25)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color("#DDD")
ax.spines["left"].set_color("#DDD")
ax.tick_params(colors="#666")

plt.tight_layout()
plt.savefig("../charts/02_intent_distribution_bar.png", bbox_inches="tight",
            facecolor=BG_COLOR)
plt.close()
print("  ✅ ../charts/02_intent_distribution_bar.png")

# ==========================================================================
# Chart 3: Top 20 Keywords — Horizontal Bar Chart
# ==========================================================================
print("📊 Generating: Top 20 Keywords Bar Chart...")

STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "must", "can", "could", "to", "of", "in",
    "for", "on", "with", "at", "by", "from", "as", "into", "through",
    "during", "before", "after", "above", "below", "between", "and",
    "but", "or", "nor", "not", "so", "yet", "both", "either", "neither",
    "each", "every", "all", "any", "few", "more", "most", "other",
    "some", "such", "no", "only", "own", "same", "than", "too", "very",
    "just", "about", "up", "out", "it", "its", "this", "that", "these",
    "those", "i", "me", "my", "we", "us", "our", "you", "your", "he",
    "him", "his", "she", "her", "they", "them", "their", "what", "which",
    "who", "whom", "when", "where", "why", "how", "there", "here",
    "if", "then", "else", "also", "still", "even", "much", "many",
    "an", "going", "get", "got", "make", "making", "go", "come",
    "take", "give", "keep", "let", "begin", "seem", "help", "show",
    "try", "ask", "need", "use",
}

all_words = []
for kw in df["Keyword"]:
    tokens = re.findall(r'\b[a-z]+\b', str(kw).lower())
    all_words.extend([t for t in tokens if t not in STOPWORDS and len(t) > 1])

word_freq = Counter(all_words).most_common(20)
words = [w for w, _ in word_freq][::-1]
freqs = [f for _, f in word_freq][::-1]

fig, ax = plt.subplots(figsize=(10, 8), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

# Gradient coloring based on frequency
norm_freqs = np.array(freqs) / max(freqs)
cmap = plt.cm.Blues
bar_colors = [cmap(0.3 + 0.7 * nf) for nf in norm_freqs]

bars = ax.barh(words, freqs, color=bar_colors, edgecolor="white",
               linewidth=1, height=0.7)

for bar, freq in zip(bars, freqs):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
            str(freq), va="center", fontsize=10, fontweight="bold", color=ACCENT)

ax.set_xlabel("Frequency", fontsize=12, color=ACCENT)
ax.set_title("Top 20 Most Repeated Keywords", fontsize=16,
             fontweight="bold", color=ACCENT, pad=15)
ax.set_xlim(0, max(freqs) * 1.12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color("#DDD")
ax.spines["left"].set_color("#DDD")
ax.tick_params(colors="#666")

plt.tight_layout()
plt.savefig("../charts/03_top_keywords_bar.png", bbox_inches="tight",
            facecolor=BG_COLOR)
plt.close()
print("  ✅ ../charts/03_top_keywords_bar.png")

# ==========================================================================
# Chart 4: Trending Concerns — Horizontal Bar Chart
# ==========================================================================
print("📊 Generating: Trending Concerns Bar Chart...")

concern_patterns = {
    "Release Date &\nAvailability": [
        r"\brelease\b", r"\bcoming out\b", r"\blaunch\b", r"\bavailab\b",
        r"\bwhen\b", r"\bdate\b", r"\b2026\b", r"\b2027\b", r"\bpre.?order\b"
    ],
    "Pricing &\nCost": [
        r"\bcost\b", r"\bprice\b", r"\bhow much\b", r"\bexpensive\b",
        r"\bcheap\b", r"\baffordable\b", r"\bbudget\b", r"\b\$\b",
        r"\bdollar\b", r"\bworth\b"
    ],
    "Specs &\nFeatures": [
        r"\bbattery\b", r"\bcamera\b", r"\bscreen\b", r"\bdisplay\b",
        r"\bprocessor\b", r"\bchip\b", r"\bram\b", r"\bstorage\b",
        r"\bsize\b", r"\bbig\b", r"\bthin\b"
    ],
    "Model\nComparisons": [
        r"\bvs\b", r"\bcompare\b", r"\bbetter\b", r"\bupgrade\b",
        r"\bdifference\b", r"\bworth\b", r"\bwait\b", r"\bor\b",
        r"\breplace\b", r"\breplacing\b"
    ],
    "Identity &\nNaming Confusion": [
        r"\bwhat is\b", r"\bwhat does\b", r"\bmean\b",
        r"\b17e\b.*\barmy\b", r"\bschool\b", r"\bdeploy\b",
        r"\bse\b", r"\bcalled\b"
    ]
}

concern_counts = {}
for name, patterns in concern_patterns.items():
    count = 0
    for kw in df["Keyword"]:
        for pat in patterns:
            if re.search(pat, str(kw).lower()):
                count += 1
                break
    concern_counts[name] = count

sorted_concerns = sorted(concern_counts.items(), key=lambda x: x[1], reverse=True)
concern_names = [c for c, _ in sorted_concerns][::-1]
concern_vals = [v for _, v in sorted_concerns][::-1]

concern_colors = ["#E74C3C", "#E67E22", "#3498DB", "#9B59B6", "#95A5A6"][::-1]

fig, ax = plt.subplots(figsize=(10, 6), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

bars = ax.barh(concern_names, concern_vals, color=concern_colors,
               edgecolor="white", linewidth=1.5, height=0.6)

for bar, val in zip(bars, concern_vals):
    pct = val / total * 100
    ax.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height()/2,
            f"{val}  ({pct:.1f}%)", va="center", fontsize=11,
            fontweight="bold", color=ACCENT)

ax.set_xlabel("Number of Queries", fontsize=12, color=ACCENT)
ax.set_title("Top 5 User Concern Areas", fontsize=16,
             fontweight="bold", color=ACCENT, pad=15)
ax.set_xlim(0, max(concern_vals) * 1.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color("#DDD")
ax.spines["left"].set_color("#DDD")
ax.tick_params(colors="#666")

plt.tight_layout()
plt.savefig("../charts/04_trending_concerns_bar.png", bbox_inches="tight",
            facecolor=BG_COLOR)
plt.close()
print("  ✅ ../charts/04_trending_concerns_bar.png")

# ==========================================================================
# Chart 5: Beginner vs Advanced — Donut Chart
# ==========================================================================
print("📊 Generating: Beginner vs Advanced Donut Chart...")

beginner_indicators = [r"\bwhat is\b", r"\bbeginner\b", r"\bbasics?\b",
                       r"\bintroduction\b", r"\btutorial\b", r"\bwhat does\b",
                       r"\bwhat are\b", r"\bhow to\b", r"\bmeaning\b",
                       r"\bmean\b", r"\bexplain\b", r"\bsimple\b",
                       r"\blearn\b", r"\bstart\b"]
advanced_indicators = [r"\boptimiz\b", r"\barchitecture\b", r"\bimplementation\b",
                       r"\bperformance\b", r"\bintegration\b", r"\badvanced\b",
                       r"\bprofessional\b", r"\bconfig\b", r"\benterprise\b",
                       r"\bbenchmark\b", r"\bantutu\b", r"\bgeekbench\b",
                       r"\bsoc\b", r"\bspecification\b"]

beginner_count = sum(1 for kw in df["Keyword"]
                     if any(re.search(p, str(kw).lower()) for p in beginner_indicators))
advanced_count = sum(1 for kw in df["Keyword"]
                     if any(re.search(p, str(kw).lower()) for p in advanced_indicators))
general_count = total - beginner_count - advanced_count

levels = ["Beginner", "Advanced", "General"]
level_counts = [beginner_count, advanced_count, general_count]
level_colors = ["#27AE60", "#E74C3C", "#BDC3C7"]

fig, ax = plt.subplots(figsize=(8, 6), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

wedges, texts, autotexts = ax.pie(
    level_counts, labels=levels,
    autopct=lambda p: f'{p:.1f}%\n({int(p*total/100)})',
    colors=level_colors, startangle=90,
    textprops={"fontsize": 12, "fontweight": "bold"},
    pctdistance=0.78,
    wedgeprops={"edgecolor": "white", "linewidth": 2, "width": 0.45}
)
for t in autotexts:
    t.set_fontsize(9)
    t.set_fontweight("bold")

ax.set_title("Beginner vs Advanced Query Distribution", fontsize=16,
             fontweight="bold", color=ACCENT, pad=20)

plt.tight_layout()
plt.savefig("../charts/05_beginner_vs_advanced.png", bbox_inches="tight",
            facecolor=BG_COLOR)
plt.close()
print("  ✅ ../charts/05_beginner_vs_advanced.png")

# ==========================================================================
# Chart 6: Modifier Type Distribution — Bar Chart
# ==========================================================================
print("📊 Generating: Modifier Type Distribution...")

mod_counts = df["Modifier Type"].value_counts()
mod_names = mod_counts.index.tolist()
mod_vals = mod_counts.values.tolist()

mod_colors = ["#3498DB", "#2ECC71", "#E74C3C", "#F39C12", "#9B59B6", "#1ABC9C",
              "#E67E22", "#95A5A6"]

fig, ax = plt.subplots(figsize=(10, 5), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

bars = ax.bar(mod_names, mod_vals, color=mod_colors[:len(mod_names)],
              edgecolor="white", linewidth=1.5, width=0.6)

for bar, val in zip(bars, mod_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            str(val), ha="center", fontsize=11, fontweight="bold", color=ACCENT)

ax.set_xlabel("Modifier Type", fontsize=12, color=ACCENT)
ax.set_ylabel("Count", fontsize=12, color=ACCENT)
ax.set_title("Query Distribution by Modifier Type", fontsize=16,
             fontweight="bold", color=ACCENT, pad=15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color("#DDD")
ax.spines["left"].set_color("#DDD")
ax.tick_params(colors="#666")
plt.xticks(rotation=15, ha="right")

plt.tight_layout()
plt.savefig("../charts/06_modifier_type_distribution.png", bbox_inches="tight",
            facecolor=BG_COLOR)
plt.close()
print("  ✅ ../charts/06_modifier_type_distribution.png")

print("\n✅ All 6 ../charts generated in ../charts/ directory!")
