## Project
https://github.com/kodigitaccount/EDA_INTEGRATION_LLM

```bash
cd EDA_INTEGRATION_LLM/EDA_LLM_Integration

# work on code.ipynb

python3.12 -m venv .venv
source .venv/bin/activate
python3.12 -m pip install --upgrade pip

python3.12 -m pip install gradio pandas matplotlib seaborn ollama

python3.12 -m gradio app.py
```

# 🍱 The "Full Meal" Project: Data, Stats & AI Integration

This repository documents the transition from structured data analysis to the integration of Generative AI and Advanced Statistics.

---

## 🥗 The "Full Meal" Concept
A complete data project is like a full meal; it requires multiple items working together:
* **The Ingredients:** `Pandas` + `Matplotlib (plt)` + `Seaborn (sns)` + `NumPy (np)`.
* **The Goal:** Ocean-depth tools (Pandas) used specifically for project results, not just theory.

---

## 🤖 LLM & Dataframe Integration
We are moving from basic data handling to **LLM + Dataset** integration to generate insights.

* **Tooling:** `Dataset` + `Ollama` + `Gemma LLM`.
* **Logic:** The LLM identifies issues (e.g., "14 missing values") in the dataframe.
* **Automation:** Instead of manual cleaning, we use a `for loop` to clean every attribute simultaneously.

---

## 🗂️ Data & AI Evolution

| Data Type | Domain | Focus Area |
| :--- | :--- | :--- |
| **Structured** | Statistics + ML | Regression, Classification, Clustering |
| **Unstructured**| AI + GenAI | LLMs, Prompts, **Agentic AI** |

> **Agentic AI:** The final stage where the AI acts as an autonomous agent to process data and solve problems.

---

## 📈 Introduction to Statistics for ML
The foundation of Machine Learning (Regression, Classification, and Clustering).

### 1. Core Statistical Concepts
* **Population vs. Sample:** Analyzing the whole group vs. a representative subset.


[Image of population vs sample in statistics]

* **Descriptive Statistics:** Summarizing data (Mean, Median, Mode).
* **Inferential Statistics:** Making predictions about a population.
* **Advanced Stats:** R-squared ($R^2$), Adjusted $R^2$, and ANOVA.

### 2. Error Metrics (Evaluation)
To check if the code and model are working correctly, we monitor:
* **MAE:** Mean Absolute Error.
* **MSE:** Mean Squared Error.
* **RMSE:** Root Mean Squared Error.
* **Type 1 & Type 2 Errors:** Understanding false positives and false negatives.



---

## 🛠️ Project Maintenance
* **Organization:** Create and fix folders to store clean data and code.
* **Debugging:** Check the code daily. If the code is not working, ask immediately to ensure the workflow from Day 1 remains functional.

---

## 🎓 Summary of Model Types
1. **Regression:** For continuous numerical predictions.
2. **Classification:** For categorical labels.
3. **Clustering:** For grouping unlabeled data.
