## Pandas & Data Science Fundamentals: Study Notes

### 🏗️ Pandas Data Structures

Pandas is built on two primary objects for handling data:

* **Series (1D):** Represents a single column or row.
* **DataFrame (2D):** A tabular structure (Rows  Columns) similar to an Excel sheet.

#### **Selection Syntax**

* `df['column']`: Single bracket returns a **Series**.
* `df[['column']]`: Double brackets return a **DataFrame**.

---

### 🗂️ The Data Landscape

Industry data determines the path of your AI model:

| Data Category | AI Path | Formats | Examples |
| --- | --- | --- | --- |
| **Structured** | Machine Learning | CSV, SQL, Excel | Tabular (Rows  Columns) |
| **Unstructured** | GenAI / Deep Learning | PDF, JPG, MP3, JSON | Images, Voice, Video, Text |

---

### 🐼 DataFrame Mastery: Inspection & Cleaning

Before analyzing data, you must understand its structure and quality.

#### **Exploration Commands**

* `df.head()` / `df.tail()`: Preview the data.
* `df.shape`: Returns `(rows, columns)`. **Axis 0** = Rows; **Axis 1** = Columns.
* `df.info()`: Crucial check for data types (Dtype) and memory usage.
* `df.columns`: Returns the names of all **Attributes/Features**.

#### **Data Preprocessing**

* **Null Values:** Identify gaps using `df.isnull().sum()`.
* **Object Types:** Pandas loads text as `object` by default; convert these to `category` for efficient visualization.

---

### 📈 Statistical Analysis

#### **Descriptive Statistics (`df.describe()`)**

Calculates the "health" of your dataset (Mean, Median, Standard Deviation, etc.).

* **Note:** By default, it only processes **Numerical Data**.
* **Insight:** Helps identify outliers or skewed distributions in your features.

#### **Univariate Analysis**

* **Goal:** Analyze **one variable** at a time to see its frequency and distribution.
* **ML Impact:** The success of your model depends on how these individual variables are distributed (e.g., checking if one team in the IPL dataset has a disproportionately high win count).

---

### 💡 Professional Guidelines

* **The Axis Rule:** Always specify `axis=0` for row-level operations and `axis=1` for column-level operations.
* **Logic over Syntax:** Do not memorize code; focus on using `df.info()` and `df.describe()` to find the "holes" in messy, real-world data.
* **Sprint Goal:** Use these four days to master the flow of data from raw tables into clean, visualized insights.
