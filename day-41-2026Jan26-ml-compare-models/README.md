# Polynomial Regression & Machine Learning Model Selection

## 1. Polynomial Regression – Overview

Polynomial Regression is an extension of **Linear Regression** where we increase the **degree of the independent variable** to model non-linear relationships.

### Mathematical Representation

y = b1·x + b2·x² + b3·x³ + … + bn·xⁿ

Example:
b1x1 + b2x1² + b3x1³

- Degree 1 → Linear Regression  
- Degree ≥ 2 → Polynomial Regression  

Increasing the degree increases model flexibility but may lead to **overfitting**.

---

## 2. Dataset Terminology

Dataset attributes are also called:

- Business Property  
- Dimension  
- Feature  
- Variable  

### Variable Types
- **Independent Variable (IV / X)** – input
- **Dependent Variable (DV / y)** – output

---

## 3. Identify the Problem Type

Based on the **Dependent Variable (DV)**:

- **Regression** → Continuous output  
  - Example: Salary, Price, Marks
- **Classification** → Categorical output  
  - Example: Yes/No, Fraud/Not Fraud

---

## 4. Classification Models

If the problem is a **classification model**, common algorithms are:

- Logistic Regression  
- Support Vector Machine (SVM)  
- Decision Tree (DT)  
- Random Forest (RF)  
- XGBoost  
- LightGBM (LGBM)  
- K-Nearest Neighbors (KNN)  

---

## 5. Model Selection Strategy

1. Train multiple ML models  
2. Evaluate model performance (Accuracy, Precision, Recall, etc.)  
3. Compare all model scores  
4. Select the **highest-performing model**  
5. Deploy the selected model  

One project can include **all ML models**, compare their scores, and finalize the best one.

---

## 6. Linear vs Polynomial Regression Example

### Linear Regression
- Employee Level: 6.5  
- Degree: 1  
- Predicted Salary: 330  

### Polynomial Regression Predictions

| Degree | Predicted Salary |
|------|------------------|
| 2 | 189 |
| 3 | 133 |
| 4 | 158 |
| 5 | 174.8 |

Polynomial Degree 5 gives a more realistic prediction compared to linear regression.

---

## 7. Overfitting & Underfitting

- **Underfitting**
  - Model is too simple
  - Cannot capture data patterns

- **Overfitting**
  - Model is too complex
  - Learns noise instead of actual patterns

In this example, the data is **not split into training and testing**, so overfitting risk exists.

---

## 8. Real-World HR Use Case

### Business Scenario
1. Company has employee salary dataset  
2. One employee quits  
3. No physical HR team  
4. Company wants to introduce AI agents  

### Models Used
- Linear Regression → 6.5 level → 330  
- Polynomial Regression (Degree 5) → 174.8  
- SVR Model  
- KNN Model  
- Decision Tree Model  
- Random Forest Model  

---

## 9. Regression vs Classification Algorithms

### Regression Models
- SVR (Support Vector Regressor)  
- KNN Regressor  
- Decision Tree Regressor  
- Random Forest Regressor  

### Classification Models
- SVM Classifier  
- KNN Classifier  
- Decision Tree Classifier  
- Random Forest Classifier  

---

## 10. Deployment

After selecting the best model:

- Save the trained model  
- Deploy using:
  - REST API
  - Web Application
  - AI Agent
- Use the model for real-time predictions

---

## Key Takeaway

Polynomial Regression is useful for non-linear data, but choosing the right degree and validating the model is essential to balance **accuracy**, **overfitting**, and **generalization**.
