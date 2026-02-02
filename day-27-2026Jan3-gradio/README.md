
## What Is Gradio?

**Gradio** is an open-source Python library that allows you to quickly build web-based user interfaces for machine learning models, APIs, and any Python functions—without writing frontend code (HTML/CSS/JavaScript).

It is widely used for:
- Rapid ML/AI prototyping
- Model demos and experimentation
- Interactive tools for data science and GenAI
- Sharing applications with teams or stakeholders

Official website: https://gradio.app  
GitHub repository: https://github.com/gradio-app/gradio

---

## Why Use Gradio?

- Very fast setup
- Pure Python (no frontend knowledge required)
- Supports rich inputs and outputs (text, image, audio, dataframe, chat, etc.)
- Runs locally and can be shared publicly
- Ideal for ML, LLMs, agents, and EDA tools

---

## Quick Start

```bash
cd /Users/venkat/workspace/gitRepos/python-genAi-agenticAI/day-27-2026Jan3-EDA

python3.12 -m venv .venv
source .venv/bin/activate
python3.12 -m pip install --upgrade pip

python3.12 -m pip install --upgrade gradio

python3.12 gradio_test.py
```

Open your browser and visit: http://localhost:7860

# 🧹 Project Data Cleaning & EDA Workshop

This section documents the transition from raw employee data to clean, system-ready datasets and the 7 foundational techniques of Exploratory Data Analysis (EDA).

---

## 🔄 Data Cleaning Workflow
1. **Raw Data:** Contains expressions and noisy characters (e.g., `|`, `;`).
2. **Memory Storage:** The data is cleaned of noisy characters and stored in the system memory as `clean_data`.
3. **System Output:** The `clean_data` is then moved from memory back to the system for final use.

---

## 📊 The 7 Techniques of EDA
These techniques are the foundation for any Data Analyst to shape their career and improve ML model accuracy (often demonstrated via Gradio by removing outliers).

1. **Variable Identification:** Identifying the type and role of each variable.
2. **Univariate Analysis:** Analyzing a single variable to understand its distribution.
3. **Bivariate Analysis:** Analyzing two variables to find relationships (e.g., **+ve Correlation**).
4. **Missing Value Treatment:** * **Numerical:** Using Mean, Median, or Mode.
    * **Categorical:** Using Mode.
5. **Outlier Treatment:** Identifying and removing anomalies to boost model performance.
6. **Variable Creation:** Generating new features from existing data.
7. **Variable Imputation:** Finalizing the filling of missing or transformed data.

---

## 🎓 Learning Resources (Workshops)

To master these techniques, refer to the following workshops:

| Topic | Link |
| :--- | :--- |
| **EDA Workshop** | [Watch on YouTube](https://www.youtube.com/watch?v=tTT7XJO30cM&t=4358s) |
| **Matplotlib Workshop** | [Watch on YouTube](https://www.youtube.com/watch?v=ChJEb5Usxug&t=3958s) |
| **Seaborn Workshop** | [Watch on YouTube](https://www.youtube.com/watch?v=JhfTZ1QWN6A&t=4561s) |

---

## 📈 Impact
* **Data Analyst Role:** Mastering these 7 steps is what shapes a professional career in data.
* **Accuracy:** Removing outliers and treating variables directly increases ML model accuracy.
