# Machine Learning: Regression & Classification Comprehensive Guide

## 1. Regression Model Comparison
In real-world implementation, we run multiple algorithms on the same dataset to compare performance based on specific hyperparameters.

### Model Ranking Table (Example: Employee Database)
| Model | Configuration | Score/Error |
| :--- | :--- | :---: |
| **KNN Regressor** | neighbors = 4 | 190.0 |
| **Polynomial Regression** | degree = 5 | 174.8 |
| **SVR** | kernel = 'poly', degree = 5 | 164.0 |
| **Random Forest (RFR)** | default | 158.0 |
| **Decision Tree (DTR)** | default | 150.0 |

---

## 2. Classification Fundamentals

### The Confusion Matrix
The confusion matrix is calculated by comparing **Actual Data ($y\_test$)** against **Predicted Data ($y\_pred$)**.



| | Predicted: YES | Predicted: NO |
| :--- | :--- | :--- |
| **Actual: YES** | **TP** (True Positive) | **FN** (False Negative) |
| **Actual: NO** | **FP** (False Positive) | **TN** (True Negative) |

### Performance Metrics
* **Accuracy:** $\frac{TP + TN}{TP + TN + FP + FN}$
* **Error Rate:** $\frac{FP + FN}{Total}$
    * *Type 1 Error:* False Positive (FP)
    * *Type 2 Error:* False Negative (FN)
* **Precision:** $\frac{TP}{TP + FP}$ 
* **Recall:** $\frac{TP}{TP + FN}$
* **F1 Score:** $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$

---

## 3. Fit Analysis (Bias vs. Variance)

| Metric | Underfitting | Overfitting | Best Fit |
| :--- | :--- | :--- | :--- |
| **Cause** | Too few attributes | Too many attributes | Relevant attributes |
| **Bias (Train)** | High | Low | Low |
| **Variance (Test)**| Low | High | Low |
| **Solution** | Add relevant features | PCA, Regularization, Dropout | Cross-Validation |

---

## 4. Algorithm Roadmap

### Classification Algorithms
* **Logistic Regression:** Uses the **Sigmoid Activation Function** to map probabilities.
* **KNN Classifier:** Instance-based learning.
* **SVM Classifier:** Support Vector Machines.
* **Naive Bayes:** Probability-based concept.

### Tree-Based & Ensemble Learning
* **Decision Tree:** Single tree logic.
* **Ensemble Learning:**
    * **Bagging:** e.g., Random Forest.
    * **Boosting:** e.g., XGBoost, LightGBM (LGBM).

---

## 5. Implementation Insights
* **Probability Concept:** Two main algorithms follow probability: **Logistic Regression** and **Naive Bayes**.
* **The Sigmoid Curve:** In Logistic Regression, the Sigmoid function maps any real-valued number into a value between 0 and 1, allowing for binary classification.
