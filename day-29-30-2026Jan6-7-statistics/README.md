## Statistics Fundamentals for Data Science

### 1. Population vs. Sample

In statistics, we differentiate between the entire group and the subset we actually study.

* **Population:** The entire group you want to draw conclusions about. (Represented by **Parameters**)
* **Sample:** A specific group that you collect data from. (Represented by **Statistics**)
* **Note:** In real-world data science, **90% of the time** we work with Sample data.

| Term | Population (Parameter) | Sample (Statistic) |
| --- | --- | --- |
| **Mean** |  (Mu) |  (x-bar) |
| **Variance** |  (Sigma squared) |  |
| **Std Deviation** |  |  |

> **Sampling:** Moving from Population  Sample.
> **Inference:** Moving from Sample  Population.

---

### 2. Descriptive Statistics

Used to summarize and describe the features of a dataset. In Python, this is often handled via `df.describe()`.

#### **A. Measures of Central Tendency**

* **Mean:** Average value.
* **Median:** Middle value when data is sorted.
* **Mode:** Most frequent value.

#### **B. Measures of Symmetry (Shape)**

**Skewness**

* **Positive Skew (+ve):** Mean > Median > Mode. Data is clustered on the **left**; the long tail is on the **right**.
* **Zero Skew:** Mean = Median = Mode. Perfectly centered (**Normal / Gaussian Distribution**).
* **Negative Skew (-ve):** Mode > Median > Mean. Data is clustered on the **right**; the long tail is on the **left**.

**Kurtosis**
Describes the "peakedness" or thickness of the tails.

* **Mesokurtic (0 Kurtosis):** Normal distribution.
* **Leptokurtic (+ve Kurtosis):** Sharp peak, heavy tails.
* **Platykurtic (-ve Kurtosis):** Flat peak, thin tails.

#### **C. Measures of Variability**

* **Variance:** The spread of data points around the mean.
* **Standard Deviation:** The square root of variance; indicates how much the data deviates from the average.

---

### 3. Inferential Statistics & Probability

Drawing conclusions about a population based on a sample.

* **Probability:** The likelihood of an event occurring (e.g., rolling a single die = ).
* **Uniform Distribution:** Every outcome has the same probability (e.g., a single die roll).
* **Normal Distribution:** The "Bell Curve" where most observations cluster around the central peak.
* **Central Limit Theorem:** As you add more dice (or samples), the distribution of the sum/mean approaches a **Normal Distribution**, even if the original data wasn't normal.

---

### 4. Confidence Intervals (CI)

A range of values where we expect a population parameter to fall.

* **The Error Term ():** * If Confidence = 95%, then  (Significance Level) = **5% (0.05)**.
* If Confidence = 99%, then  = **1% (0.01)**.



| Scenario | Test Type |
| --- | --- |
| Population Variance () is **Known** | **Z-test** |
| Population Variance () is **Unknown** | **T-test** (uses Sample Variance) |

---

### 5. Advanced Evaluation Metrics

#### **Regression Metrics (Predicting Numbers)**

* ** (Coefficient of Determination):** How well the model explains the variance.
* **Adjusted :** Penalizes the model for adding useless predictors; prevents overfitting.
* **MAE / MSE / RMSE:** Measure the distance between predicted and actual values.

#### **Classification Metrics (Predicting Categories)**

* **Confusion Matrix:** A  table showing True Positives, True Negatives, False Positives, and False Negatives.
* **Type 1 Error:** False Positive (Rejecting a true Null Hypothesis).
* **Type 2 Error:** False Negative (Failing to reject a false Null Hypothesis).
