# AI Agent Experiment: Search Intent & Query Analysis

## 🎯 Objective

Analyze public search queries from **AnswerThePublic** (exported datasets: `./data/Data01.xlsx` and `./data/Data02.csv`) to:

- Classify search intent
- Identify keyword patterns
- Detect user concerns
- Propose an application component

---

# 🧪 Experiment Workflow

---

# Step 01: Data Collection

## Input

- Dataset files: `./data/Data01.xlsx` and `./data/Data02.csv`
- Source: AnswerThePublic (already exported)

## Task 1.1 – Load Dataset

- Load `./data/Data01.xlsx` and `./data/Data02.csv`
- Merge/combine both datasets into a single unified dataframe
- Identify relevant columns (e.g., Query, Search Term, Keyword, Question)
- Clean data:
  - Remove null values
  - Remove duplicates
  - Standardize text (lowercase, trim spaces)

---

## Task 1.2 – Categorize Search Intent

Classify each query into one of the following:

| Category      | Definition                           | Example Indicators              |
| ------------- | ------------------------------------ | ------------------------------- |
| Informational | User wants knowledge                 | what, why, how, guide, tutorial |
| Navigational  | User looking for specific site/brand | login, website, near me         |
| Transactional | User ready to buy/act                | buy, price, order, download     |
| Comparative   | User comparing options               | vs, best, better, alternative   |

### AI Agent Instructions:

- Use rule-based classification first.
- Optionally use NLP intent classification if needed.
- Add a new column: `Intent_Category`

---

# Step 02: Data Analysis

---

## Task 2.1 – Count Queries per Category

Generate:

- Total queries
- Count per category
- Percentage distribution

Output:

- Summary table
- Pie chart (if dashboard selected)

---

## Task 2.2 – Identify Most Repeated Keywords

Steps:

- Tokenize queries
- Remove stopwords
- Count word frequency
- Extract Top 20 keywords

Output:

- Frequency table
- Word cloud (optional)

---

## Task 2.3 – Detect Trending Concerns

Analyze:

- Frequently repeated phrases
- Negative sentiment words (problem, issue, not working, error)
- Confusion indicators (how to, why does, can't)

Deliver:

- Top 5 Concern Areas
- Supporting example queries

---

## Task 2.4 – Pattern Analysis

Identify:

### A) Beginner-Level Queries

Indicators:

- what is
- beginner
- basics
- introduction
- tutorial

### B) Advanced-Level Queries

Indicators:

- optimization
- architecture
- implementation
- performance
- integration

Output:

- % Beginner vs Advanced
- Insight summary

---

# Step 03: Application Component

Based on findings, choose ONE option:

---

# OPTION I — Content Strategy

## Deliverables:

### 1️⃣ Blog Plan (10 Titles)

- Titles based on most common informational queries
- Optimized for SEO
- Aligned with high-frequency keywords

### 2️⃣ FAQ Page

- 15 real user questions
- Structured Q&A format
- Organized by intent category

### 3️⃣ SEO Outline

- Target keyword clusters
- H1, H2, H3 structure
- Meta description suggestions

---

# OPTION II — Product Feature Proposal

Choose ONE:

## A) AI Chatbot Proposal

Design:

- Intent-aware chatbot
- Pre-trained on most common queries
- Fallback mechanism for unknown questions
- Architecture diagram (conceptual)

## B) Knowledge Base System

Design:

- Categorized articles
- Search functionality
- Auto-suggestion engine
- Tag-based filtering

## C) Learning Path Recommender

Design:

- Beginner to Advanced progression
- Personalized content recommendations
- Skill tagging system
- Adaptive learning logic

Deliver:

- Problem Statement
- Proposed Solution
- System Architecture (High-level)
- Expected Impact

---

# OPTION III — Dashboard Development

Create:

## Jupyter Notebook (.ipynb)

Include:

### 1️⃣ Data Preprocessing

- Load ./data/Data01.xlsx and ./data/Data02.csv
- Merge/combine both datasets
- Cleaning & intent tagging

### 2️⃣ Visualizations

- Bar chart: Intent distribution
- Pie chart: Search intent %
- Word frequency bar chart
- Beginner vs Advanced comparison

### 3️⃣ Insights Section

- Written summary
- Key patterns discovered

Libraries Allowed:

- pandas
- matplotlib
- seaborn (optional)
- nltk / sklearn (optional)

---

# 📊 Final Output Requirements

AI Agent must generate:

1. Cleaned dataset (with intent column)
2. Summary statistics
3. Keyword frequency table
4. Pattern analysis report
5. One selected application component
6. Clear conclusion section

---

# 🧠 Evaluation Criteria

| Criteria                      | Weight |
| ----------------------------- | ------ |
| Correct Intent Classification | 25%    |
| Quality of Pattern Analysis   | 25%    |
| Insight Depth                 | 20%    |
| Application Design Quality    | 20%    |
| Clarity & Presentation        | 10%    |

---

# 📝 Expected Final Structure

```
1. Introduction
2. Dataset Description
3. Intent Classification Results
4. Keyword Analysis
5. Pattern & Concern Analysis
6. Application Component
7. Conclusion
```
