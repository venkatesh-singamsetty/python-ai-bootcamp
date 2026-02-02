## Statistics
Here is the organized content for your Markdown file. You can copy the block below and save it as a `.md` file (e.g., `Statistics_Notes.md`).

---

# Statistics Fundamentals for Data Science

## 1. Population vs. Sample

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

## 2. Descriptive Statistics

Used to summarize and describe the features of a dataset. In Python, this is often handled via `df.describe()`.

### A. Measures of Central Tendency

* **Mean:** Average value.
* **Median:** Middle value when data is sorted.
* **Mode:** Most frequent value.

### B. Measures of Symmetry (Shape)

#### Skewness

* **Positive Skew (+ve):** Mean > Median > Mode. Data is clustered on the **left**; the long tail/outliers are on the **right**.
* **Zero Skew:** Mean = Median = Mode. Data is perfectly centered (**Normal Distribution / Gaussian Distribution**).
* **Negative Skew (-ve):** Mode > Median > Mean. Data is clustered on the **right**; the long tail/outliers are on the **left**.

#### Kurtosis

Describes the "peakedness" or thickness of the tails.

* **Mesokurtic (0 Kurtosis):** Normal distribution.
* **Leptokurtic (+ve Kurtosis):** Sharp peak, thin spread (heavy tails).
* **Platykurtic (-ve Kurtosis):** Flat peak, wide spread (thin tails).

### C. Measures of Variability

* **Variance:** The spread of data points around the mean.
* **Standard Deviation:** The square root of variance; indicates how much the data deviates from the average.

---

## 3. Inferential Statistics

Drawing conclusions about a population based on a sample.

* **Probability:** The likelihood of an event occurring (e.g., rolling a die = , flipping a coin = ).
* **Distributions:** Patterns formed by probability.
* **Uniform Distribution:** Every outcome has the same probability (e.g., rolling a single die).
* **Normal Distribution:** The "Bell Curve" where most observations cluster around the central peak.


* **Outlier Adjustment:** Using probability and distributions to identify and handle data points that fall too far from the mean.

---

## 4. Advanced Statistics & Evaluation Metrics

### Statistical Tests & Concepts

* **ANOVA:** Analysis of Variance; used to compare means between three or more groups.
* **Type 1 Error:** False Positive (Rejecting a true Null Hypothesis).
* **Type 2 Error:** False Negative (Failing to reject a false Null Hypothesis).

### Regression Metrics

* ** (Coefficient of Determination):** How well the model explains the variance of the data.
* **Adjusted :** Modified version of  that accounts for the number of predictors in the model.
* **MAE (Mean Absolute Error):** Average of the absolute differences between predicted and actual values.
* **MSE (Mean Squared Error):** Average of the squared differences; penalizes larger errors.
* **RMSE (Root Mean Squared Error):** Square root of MSE; brings the error unit back to the original scale.

---

### Python Tools

* **Pandas/NumPy:** Data manipulation and basic stats.
* **SciPy:** Advanced scientific computing and statistical tests.

---

**Would you like me to generate a Python script that calculates these metrics (like Skewness, Kurtosis, and RMSE) using a sample dataset?**

It looks like you've put together a solid set of study notes on statistics and machine learning! There are a few key technical points to clarify, especially regarding the **sum of two dice** and the **Normal distribution**, to make sure your foundation is rock-solid.

Here is a cleaned-up, structured version of your notes in Markdown format.

---

## 1. Probability & Dice Rolls

* **Total Outcomes:** While one die has 6 sides, rolling **two dice** results in  possible combinations. The sum of these dice ranges from **2 to 12**.
* **The Probability of rolling a 1:** If you roll two standard dice, the probability of getting a **sum of 1** is **0%** (since the minimum sum is ).
* **Distributions:**
* **Single Die:** Follows a **Uniform Distribution** (every side has a  chance).
* **Two Dice (Sum):** This follows a **Triangular Distribution**, not quite a Normal distribution yet. However, as you add *more* dice, the distribution starts to look like a **Normal (Gaussian) Distribution** due to the **Central Limit Theorem**.



---

## 2. Confidence Intervals (CI)

A Confidence Interval is a range of values where we expect a population parameter to fall, based on a specific level of certainty.

* **The Logic:** If a student is 95% confident they scored between 80–90, and they get an 85, the "estimate" was successful.
* **The Error Term ():** * If Confidence = 95%, then  (Significance Level) = **5% (0.05)**.
* If Confidence = 99%, then  = **1% (0.01)**.


* **The Formula Components:**
* **Lower Bound:** 
* **Upper Bound:** 



### Choosing the Test

| Scenario | Test Type |
| --- | --- |
| Population Variance () is **Known** | **Z-test** |
| Population Variance () is **Unknown** | **T-test** (uses Sample Variance) |

---

## 3. Standard Error (SE)

Standard error measures the accuracy with which a sample represents a population.

> **Note:** As your sample size () increases, your error decreases. This is why researchers prefer larger sample sizes!

---

## 4. Model Validation Metrics

Once you build a Machine Learning model, you must test its performance:

### Regression (Predicting Numbers)

* **R-Squared ():** How much of the variance is explained by the model.
* **Adjusted R-Squared:** A better version of  that accounts for the number of predictors (prevents overfitting).

### Classification (Predicting Categories)

* **Accuracy Score:** Overall correctness.
* **Confusion Matrix:** A table used to describe the performance of the model (True Positives, False Positives, etc.).

---

**Would you like me to explain the difference between R-squared and Adjusted R-squared with a practical example?**
