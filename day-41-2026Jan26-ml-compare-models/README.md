## 📈 Polynomial Regression & Model Selection: Study Notes

This guide covers the transition from basic linear models to flexible non-linear regressions and the strategic framework for selecting the best machine learning algorithm for any business problem.

---

## 1. Polynomial Regression – Modeling Curvature

Polynomial Regression is used when the relationship between data points is **non-linear**. Instead of a straight line, we create a curve by increasing the power (degree) of the independent variable.

### Mathematical Representation

* **Degree 1:** Standard Linear Regression (Straight Line).
* **Degree 2+:** Polynomial Regression (Curved Line).
* **Trade-off:** Higher degrees offer more flexibility but significantly increase the risk of **overfitting**.

---

## 2. Identify the Problem: Regression vs. Classification

The first step in any ML project is looking at your **Dependent Variable (DV)** to define the task.

| Task | Output Type (DV) | Examples |
| --- | --- | --- |
| **Regression** | **Continuous Numbers** | Salary, Temperature, Stock Price, House Value. |
| **Classification** | **Discrete Categories** | Spam/Not Spam, Fraud/Legal, Grade A/B/C. |

---

## 3. Algorithm Library: Regressors vs. Classifiers

Most major ML algorithms have two "flavors": one for predicting numbers and one for predicting labels.

| Algorithm | For Regression (Numbers) | For Classification (Labels) |
| --- | --- | --- |
| **Support Vector Machine** | SVR | SVC |
| **K-Nearest Neighbors** | KNN Regressor | KNN Classifier |
| **Decision Tree** | Decision Tree Regressor | Decision Tree Classifier |
| **Random Forest** | Random Forest Regressor | Random Forest Classifier |

---

## 4. Overfitting & Underfitting

The goal of ML is to find the "Sweet Spot" where the model generalizes well to new, unseen data.

* **Underfitting:** The model is too simple (e.g., using a straight line for curved data). High error on both training and testing sets.
* **Overfitting:** The model is too complex (e.g., a Degree 20 Polynomial). It "memorizes" the training data, including noise, but fails on real-world data.

---

## 5. Model Selection & Deployment Strategy

In a professional setting, we don't just pick one model; we run an "audit" of several models to find the champion.

1. **Preparation:** Define  (Features) and  (Target).
2. **Training:** Fit multiple models (SVR, KNN, Random Forest, etc.) to the training data.
3. **Evaluation:** Compare performance metrics ( or RMSE for Regression; Accuracy or F1-score for Classification).
4. **Selection:** Finalize the model with the highest score.
5. **Deployment:** * **Save:** Serialize the model (e.g., using `.pkl`).
* **Integration:** Deploy via REST API, Web App (Streamlit/Flask), or AI Agent.

---

## 6. Real-World Case: HR Salary Prediction

**Scenario:** Predicting the salary for a "Level 6.5" employee based on historical data.

* **Linear Regression:** Predicted 330k (Too high; assumes a straight line).
* **Polynomial (Degree 5):** Predicted 174.8k (More realistic; follows the curve of typical corporate raises).
* **Business Impact:** Using the Polynomial model prevents the company from overpaying while remaining competitive enough to hire.
