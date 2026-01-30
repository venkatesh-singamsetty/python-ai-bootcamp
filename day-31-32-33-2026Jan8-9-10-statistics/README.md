# 📘 COMPLETE STATISTICS NOTES (6th – 9th + ML CONNECTION)
- https://www.youtube.com/watch?v=baJi1276DcU

These notes are a **complete, detailed, classroom-to-industry conversion** of all concepts discussed.
Designed for:
- Learning from scratch
- ML understanding
- Interviews
- Real-world use cases

---

## 1️⃣ Population vs Sample

### Population
- Entire group/data
- Mean = μ (Mu)
- Variance = σ²
- Parameters

### Sample
- Subset of population
- Mean = x̄
- Variance = s²
- Statistics

> 🔑 **90% of real-world data science works on SAMPLE data**

---

## 2️⃣ Sampling vs Inference

- **Sampling** → Population ➜ Sample  
- **Inference** → Sample ➜ Population  

---

## 3️⃣ Descriptive Statistics  
(Used to DESCRIBE data)

Python:
```python
df.describe()
```

### A. Measure of Central Tendency
- Mean → Average
- Median → Middle value
- Mode → Most frequent value

---

### B. Measure of Symmetry (Skewness)

| Type | Condition | Meaning |
|----|----|----|
| +ve skew | Mean > Median > Mode | Data left, outlier right |
| 0 skew | Mean = Median = Mode | Perfect symmetry |
| -ve skew | Mode > Median > Mean | Data right, outlier left |

📌 **0 skew distribution =**
- Normal Distribution
- Gaussian Distribution
- Bell Curve

---

### C. Kurtosis (Peakedness)

| Type | Description |
|----|----|
| Platykurtic | Flat curve |
| Mesokurtic | Normal |
| Leptokurtic | Sharp peak |

Classroom Mapping:
- +ve skew → Platykurtic
- -ve skew → Leptokurtic
- 0 skew → Mesokurtic

⚠️ Always try to make data **close to normal distribution**

---

### D. Measure of Variability
- Variance → Spread around mean
- Standard Deviation → √Variance

Population vs Sample:
- Population variance = σ²
- Sample variance = s²

---

## 4️⃣ Inferential Statistics

Used to **predict & decide**
- Probability
- Distribution
- Confidence Interval
- Hypothesis Testing

---

## 5️⃣ Probability & Distribution

### Dice Example 🎲
- Dice has 6 sides
- Probability of each number = 1/6
- One dice → Uniform Distribution

### Two Dice 🎲🎲
- Outcomes form a bell curve
- Middle values occur more
- Distribution becomes NORMAL

📌 **Distribution is born from probability**

---

## 6️⃣ Confidence Interval (CI)

> “I am 95% confident the true value lies in this range”

### Example
- Exam went well
- 95% confidence → Score between 80–90
- Actual score = 85 → Confidence accepted

### CI Components
- Lower Confidence Limit
- Upper Confidence Limit

---

### Z-Test vs T-Test

| Scenario | Test |
|----|----|
| Population variance known | Z-test |
| Population variance unknown | T-test |

📌 **99% real-world problems use T-test**

---

## 7️⃣ Standard Error
SE = σ / √n

---

## 8️⃣ Z-Score & Z-Table

### Z-Score
- Converts data to:
  - Mean = 0
  - Std Dev = 1

ML Mapping:
- ML → Feature Scaling / Standardization
- Time Series → White Noise

### Z-Table
- Used to calculate Z-test values

---

## 9️⃣ Hypothesis Testing

### Statement Example
"Apples are expensive in Hyderabad"

Hypothesis:
- 1kg apple cost = ₹2000

### Types
- Null Hypothesis (H₀)
- Alternative Hypothesis (H₁)

### Decision
| Sample Mean | Decision |
|----|----|
| 200 | Reject H₀ |
| 1800 | Accept H₀ |

---

### P-Value
- Threshold = 0.05
- p < 0.05 → Reject H₀
- p ≥ 0.05 → Accept H₀

---

## 🔗 Statistics ↔ Machine Learning

### Regression (ML)

Error terms:
```
Error = Actual − Predicted
Residual = Loss = Cost
```

#### Metrics
- MAE = mean(|A − P|)
- MSE = mean((A − P)²)
- RMSE = √MSE

### R² & Adjusted R²
- Range: 0 to 1
- Higher = Better regression model

---

### Classification Model

Performance Measure:
**Confusion Matrix**

| Term | Meaning |
|----|----|
| TP | True Positive |
| TN | True Negative |
| FP | False Positive |
| FN | False Negative |

📌 After this matrix — *no more confusion*

---

## 10️⃣ ANOVA
- Used to compare multiple means
- Helps in feature relevance

