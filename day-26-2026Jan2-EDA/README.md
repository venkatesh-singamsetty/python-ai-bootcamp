## 🧹 Data Cleaning & EDA Techniques: Study Notes

This section covers essential methods for refining raw data, specifically focusing on text cleaning with Regular Expressions (RegEx) and the logic behind handling missing data.

---

## 🔡 String Manipulation (RegEx)

Regular Expressions (RegEx) allow you to identify and replace patterns in text data, which is crucial when cleaning messy "Object" columns in Pandas.

* **Command:** `str.replace(r'\w', '')`
* **Logic:** * `\w` represents **Word Characters**: This includes all alphanumeric characters (a-z, A-Z, 0-9) and the underscore (`_`).
* **Opposite:** To target special characters (like `@`, `#`, `!`), you would use the uppercase `\W` (Non-word characters).

---

## 🛠️ EDA Technique: Missing Value Treatment

In Exploratory Data Analysis, "Imputation" is the process of filling in gaps where data was not recorded.

### 1. Numerical Values

Numerical data (Integers/Floats) is handled using the "Center" of the data distribution:

* **Mean:** The mathematical average. Best for data that is **Normally Distributed** (Symmetrical).
* **Median:** The middle value. Best when the data has **Outliers**, as the median is not skewed by extreme values.
* **Mode:** The most frequent number. Rarely used for numbers, but helpful for discrete counts.

### 2. Categorical Values

Categorical data (Strings/Labels) cannot be averaged.

* **Mode:** We identify the most frequently occurring category (e.g., if "Mumbai Indians" appears most often in an IPL dataset, we use it to fill missing team entries).

---

## 📊 Summary Table: Imputation Strategy

| Data Type | Primary Treatment | Secondary Treatment |
| --- | --- | --- |
| **Numerical** | **Mean** (Normal data) | **Median** (Skewed data/Outliers) |
| **Categorical** | **Mode** (Most Frequent) | Constant value (e.g., "Unknown") |
| **Text Cleaning** | **RegEx** (`\w`) | String slicing / stripping |

---

## 💡 Pro-Tip for Data Analysts

Always check the **Skewness** of your data before choosing a treatment. If you use the **Mean** on data with heavy outliers (like salary data where one person earns millions), your "average" will be misleadingly high. In such cases, the **Median** provides a more truthful representation.
