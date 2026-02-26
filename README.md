# AI Agent Experiment: Search Intent & Query Analysis (iPhone 17e)

## 🎯 Objective

This project analyzes public search queries related to the **iPhone 17e** sourced from AnswerThePublic. The goal is to classify search intent, identify keyword patterns, detect user concerns, and propose an actionable content strategy.

## 📁 Project Structure

- [Report.md](./Report.md): Detailed analysis and final findings.
- [code/](./code/): Python scripts for data processing (`experiment.py`) and visualization (`visualize.py`).
- [data/](./data/): Source datasets and cleaned output.
- [charts/](./charts/): Generated visualizations of the data analysis.
- [INSTRUCTIONS.md](./INSTRUCTIONS.md): Original experiment requirements and workflow.

## 🚀 Key Findings

- **Informational Dominance:** 82.4% of queries are informational, indicating users are in the research phase.
- **Top Concerns:** Release date (10.1%), Pricing (8.3%), and Specifications (8.3%) are the primary focus areas.
- **Beginner Audience:** A large proportion of users are casual consumers seeking accessible information.
- **Intent Distribution:**
  - Informational: 82.4%
  - Transactional: 11.3%
  - Comparative: 6.0%
  - Navigational: 0.3%

## 📊 Visual Analysis (Outputs)

Below are the key insights generated from the dataset:

### Intent & Modifier Distribution

![Intent Distribution — Pie Chart](./charts/01_intent_distribution_pie.png)
![Modifier Type Distribution](./charts/06_modifier_type_distribution.png)

### Keyword & Concern Trends

![Top 20 Keywords](./charts/03_top_keywords_bar.png)
![Trending Concerns](./charts/04_trending_concerns_bar.png)

## 🛠️ How to Run

1. Ensure you have the required datasets in `./data/`.
2. Run `python code/experiment.py` to clean the data and perform intent classification.
3. Run `python code/visualize.py` to generate analysis charts.

---

For a complete breakdown of the results and content strategy proposals, see the [Full Report](./Report.md).
