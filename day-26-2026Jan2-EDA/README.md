# 🧹 Data Cleaning & EDA Techniques

This section covers string manipulation using Regular Expressions and the foundational approach to Missing Value Treatment.

---

## 🔡 String Manipulation (RegEx)
Using Regular Expressions to clean text data within a string:

* **Command:** `str.replace(r'\w', '')`
* **Logic:** * `\w` targets **Word Characters** (Letters, Numbers, Underscores).
    * **Non-word characters** include special symbols (like `@`, `#`, `!`) and spaces.

---

## 🛠️ EDA Technique: Missing Value Treatment
Exploratory Data Analysis (EDA) begins with handling missing data (Imputation). We have completed one core technique:

### 1. Numerical Values
When a numerical data point is missing, it is treated using:
* **Mean:** The average of the values.
* **Median:** The middle value (often used when outliers are present).
* **Mode:** The most frequent value.



### 2. Categorical Values
When a label or category (text-based data) is missing:
* **Mode:** The most frequent category is used to fill the gap.



---

## 📊 Summary Table

| Data Type | Treatment Technique |
| :--- | :--- |
| **Numerical** | Mean, Median, or Mode |
| **Categorical** | Mode |
| **String (RegEx)** | `\w` (Word) vs Non-word characters |

---

Would you like me to provide the **Pandas code** to apply these Mean, Median, and Mode treatments to your dataset?
