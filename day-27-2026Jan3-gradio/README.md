## Gradio & EDA Workshop: Study Notes

### 🚀 What is Gradio?

**Gradio** is an open-source Python library used to build web-based interfaces for ML models and APIs without requiring frontend knowledge (HTML/CSS/JS).

* **Primary Uses:** Rapid prototyping, model demos, GenAI agents, and interactive EDA tools.
* **Key Features:** * Pure Python setup.
* Supports diverse inputs/outputs (text, images, audio, dataframes).
* Shareable via public links or local hosting.


* **Default Port:** `http://localhost:7860`

#### **Quick Start Commands:**

```bash
# Setup Virtual Environment
python3.12 -m venv .venv
source .venv/bin/activate

# Install & Run
python3.12 -m pip install --upgrade gradio
python3.12 gradio_test.py

```

---

### 🧹 Data Cleaning Workflow

Standardizing raw data into system-ready formats involves three stages:

1. **Raw Data:** Identify noisy characters (e.g., `|`, `;`) and expressions.
2. **Memory Storage:** Processing the noise to create `clean_data` within system memory.
3. **System Output:** Exporting `clean_data` from memory back to the system for final deployment.

---

### 📊 The 7 Foundational Techniques of EDA

Mastering these steps is essential for professional data analysts to improve model accuracy.

1. **Variable Identification:** Defining the role and type of each data column.
2. **Univariate Analysis:** Studying a single variable’s distribution.
3. **Bivariate Analysis:** Finding relationships between two variables (e.g., positive correlation).
4. **Missing Value Treatment:** * **Numerical:** Impute using Mean, Median, or Mode.
* **Categorical:** Impute using Mode.


5. **Outlier Treatment:** Identifying and removing anomalies to boost performance.
6. **Variable Creation:** Engineering new features from existing data.
7. **Variable Imputation:** Finalizing the replacement of missing or transformed values.

---

### 🎓 Learning Resources

| Topic | Video Link |
| --- | --- |
| **EDA Workshop** | [Watch Here](https://www.youtube.com/watch?v=tTT7XJO30cM) |
| **Matplotlib Workshop** | [Watch Here](https://www.youtube.com/watch?v=ChJEb5Usxug) |
| **Seaborn Workshop** | [Watch Here](https://www.youtube.com/watch?v=JhfTZ1QWN6A) |

---

### 📈 Final Summary

* **Professional Impact:** These 7 steps define the core competency of a Data Analyst.
* **Performance:** Proper outlier and variable treatment directly results in higher Machine Learning model accuracy.
