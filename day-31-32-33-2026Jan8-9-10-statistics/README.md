---

**Learning Resource:** [Statistics Workshop Video](https://www.youtube.com/watch?v=baJi1276DcU)

---

## 📘 Complete Statistics & ML Connection Notes

### 1️⃣ Core Concepts: Population vs. Sample

* **Population:** The entire dataset/group. (Mean: **μ**, Variance: **σ²**). These are called **Parameters**.
* **Sample:** A subset of the population. (Mean: **x̄**, Variance: **s²**). These are called **Statistics**.
* **Industry Fact:** 90% of real-world data science is performed on **Sample data**.
* **Workflows:**
* **Sampling:** Population  Sample
* **Inference:** Sample  Population

---

### 2️⃣ Descriptive Statistics (Describing Data)

Use `df.describe()` in Python to quickly view these metrics.

#### **A. Central Tendency**

* **Mean:** Average.
* **Median:** Middle value.
* **Mode:** Most frequent value.

#### **B. Symmetry & Shape (Skewness & Kurtosis)**

| Metric | Type | Condition | Industry Term |
| --- | --- | --- | --- |
| **Skewness** | **+ve Skew** | Mean > Median > Mode | Data on left, tail on right (Platykurtic) |
|  | **0 Skew** | Mean = Median = Mode | **Normal / Gaussian / Bell Curve** |
|  | **-ve Skew** | Mode > Median > Mean | Data on right, tail on left (Leptokurtic) |
| **Kurtosis** | **Mesokurtic** | Normal Peak | Standard Bell Curve |

---

### 3️⃣ Inferential Statistics (Predicting & Deciding)

#### **A. Probability & Distribution**

* **Uniform Distribution:** Outcomes have equal probability (e.g., rolling one die).
* **Normal Distribution:** Outcomes cluster in the middle (e.g., sum of two dice). Distribution is born from probability.

#### **B. Confidence Interval (CI)**

* A range where we are confident (e.g., 95%) the true value lies.
* **Z-Test:** Used when population variance is known.
* **T-Test:** Used when population variance is unknown (**99% of real-world use cases**).

#### **C. Standard Error (SE)**

* **Formula:** 

---

### 4️⃣ Hypothesis Testing

* **Null Hypothesis ():** The status quo or specific claim (e.g., Apple cost = ₹2000).
* **Alternative Hypothesis ():** The opposing claim.
* **P-Value Decision Rule:**
* **p < 0.05:** Reject .
* **p ≥ 0.05:** Accept (Fail to reject) .

---

### 5️⃣ Machine Learning Connection

#### **A. Feature Scaling (Z-Score)**

* **Z-Score:** Standardizes data so Mean = 0 and Std Dev = 1.
* **Usage:** Used in ML for **Standardization** and in Time Series to identify **White Noise**.

#### **B. Regression Metrics**

* **Error (Residual/Loss/Cost):** Actual Value  Predicted Value.
* **MAE:** Mean Absolute Error.
* **MSE:** Mean Squared Error.
* **RMSE:** Root Mean Squared Error.
* **$R^2$ & Adjusted $R^2$:** Measure how well the model fits (Range 0 to 1; higher is better).

#### **C. Classification & ANOVA**

* **Confusion Matrix:** Measures performance using:
  - **TP / TN:** True Positives / Negatives.
  - **FP / FN:** False Positives / Negatives.


* **ANOVA:** Used to compare means of multiple groups and identify **feature relevance**.
