# Pandas --- Notes

## Data Structures

-   **DataFrame**
    -   2D data structure
    -   Contains rows and columns
-   **Series**
    -   1D data structure
    -   Represents a single row or a single column

------------------------------------------------------------------------

## Column Selection

``` python
tags['tag']      # Series
tags[['tag']]    # DataFrame
```

-   **Single bracket `[ ]`**
    -   Returns a Series
-   **Double bracket `[[ ]]`**
    -   Returns a DataFrame

------------------------------------------------------------------------

## Summary

-   Series → 1D
-   DataFrame → 2D
-   `[ ]` → Series
-   `[[ ]]` → DataFrame

# 📊 Data Science & Descriptive Statistics

This section focuses on the fast-track mastery of **NumPy** and **Pandas**, distinguishing between data types, and performing initial statistical analysis.

---

## 🗂️ The Two Worlds of Data

In the industry, data is categorized into two main types, which determines whether we use Machine Learning or Advanced AI (Deep Learning/GenAI).



### 1. Structured Data (Machine Learning)
* **Type:** Labeled Data (Supervised Learning).
* **Formats:** Excel, CSV, SQL Tables.
* **Structure:** Rows × Columns (DataFrames).
* **Key Terms:** * **Attributes/Features/Variables:** The columns in your dataset.

### 2. Unstructured Data (AI / GenAI / Agentic AI)
* **Type:** Unlabeled Data (Unsupervised Learning).
* **Formats:** PDF, Images, Voice, Video, XML, JSON, BSON.
* **Handling:** Requires advanced processing (like PIL for images or LLMs for text).

---

## 🐼 Pandas: Mastering the DataFrame

When we work with data in Python, we treat Excel sheets as **Datasets** and load them into a **DataFrame**.

### Basic Exploration Commands:
* `df.head()` / `df.tail()`: View the first or last few rows.
* `df.info()`: Get a summary of the data types and memory usage.
* `df.shape`: Check the number of rows and columns (Axis 0 = Rows, Axis 1 = Columns).
* `df.columns`: List all attribute names.

### Data Cleaning & Preprocessing:
* **Handling Nulls:** `df.isnull().sum()` or `df.isna()` to find missing values.
* **Type Conversion:** Pandas captures text as an `object` by default. You must convert these to `categorical` data for proper visualization.
* **Manipulation:** Renaming attributes or adding new columns to existing tables found in the organization's database.

---

## 📈 Descriptive Statistics

To understand the "Health" of your data (like an economy where 1 earns and 9 eat vs. 8 earning), we use statistical tools.

### `.describe()` Function
* **Focus:** Provides statistical summaries (Mean, Median, Std Dev, etc.) for **Numerical Data** only.
* **Limitation:** It does not provide information for categorical attributes.



---

## 📉 Univariate Analysis
The first step in data visualization.
* **Definition:** Plotting a graph using **only one variable** to understand its distribution and frequency.
* **Analogy:** Just as a country's economy depends on the ratio of earners to non-earners, your model's success depends on the distribution of your primary features.

---

## 🚀 Pro-Tips for the 4-Day NumPy/Pandas Sprint
* **Don't Memorize:** Use the provided documentation; the goal is to understand the *logic* of the data flow.
* **Axis Rule:** Always remember **Axis 0 = Rows** and **Axis 1 = Columns**. This is essential when dropping or adding data.
* **Maturity:** Think like a professional. Data in the real world is messy—use `df.info()` and `df.describe()` early to find the "holes" in your data.

> **Next Step:** We will apply Univariate Analysis to our IPL Dataset to see which teams have the highest win frequency.
