## EDA: Machine Learning Foundations – Study Notes

This section details the critical processes required to transform raw data into a format that algorithms can process effectively.

---

### 1. Variable Identification: The "Inputs" and "Outputs"

In the data world, a column is referred to as a **Variable**, **Feature**, or **Attribute**.

* **Dependent Variable (DV / ):** The specific outcome you want to predict (e.g., Will a customer churn?).
* **Independent Variables (IV / ):** The factors that influence the outcome (e.g., Customer age, monthly bill, contract length).

---

### 2. Univariate & Bivariate Analysis

* **Univariate:** Inspecting **one** variable to find its "shape" (distribution), average (mean), and potential errors.
* **Bivariate (Correlation):** Checking the relationship between **two** variables.
* **+1.0:** Perfect Positive (Both go up together).
* **0.0:** No relationship.
* **-1.0:** Perfect Negative (One goes up, the other goes down).



---

### 3. Outlier Treatment: Managing Abnormalities

Outliers are extreme values that can "pull" the average away from the truth.

* **Detection:** Visualized best through **Boxplots**.
* **Impact:** They significantly harm algorithms like Linear Regression and KNN.
* **Professional Solution:** Instead of just deleting them (which loses data), we often use **transformation functions** like the **Sigmoid Curve** to squash extreme values between **0 and 1**.

---

### 4. Handling Missing Values

Data gaps are common in real-world projects like our **IPL Analytics** dataset.

* **Numerical Data:**
* Use **Mean** if the data is normally distributed.
* Use **Median** if there are heavy outliers.


* **Categorical Data:**
* Use **Mode** (most frequent) or **KNN Imputation**.



---

### 5. Variable Transformation (Encoding)

Since ML models only "speak" math, text-based categorical data must be converted into numbers.

| Technique | Description | Best For... |
| --- | --- | --- |
| **One-Hot Encoding** | Creates 0/1 binary columns for each category. | Non-ordered data (e.g., Team Names). |
| **Label Encoding** | Assigns a unique number (0, 1, 2) to each label. | Ordered data (e.g., Junior, Mid, Senior). |

---

### 6. Variable Creation (Feature Engineering)

The act of deriving new insights from existing columns.

* **Example:** If you have a `Date` column, you create a `Day_of_Week` column to see if IPL ticket sales are higher on Sundays.

---

### 💡 Core Summary

* **EDA is 80% of the work.**
* **Accuracy depends on data quality, not just the model.**
* **Encoding is mandatory** for non-numeric data.
