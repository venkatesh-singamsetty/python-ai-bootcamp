"""
File Name   : investment_profit_mlr_backward_elimination.py
Purpose     : Multiple Linear Regression with Backward Elimination
Dataset     : Investment.csv
Author      : Venkatesh Singamsetty
Description :
    - Handles categorical data with One-Hot Encoding
    - Performs Multiple Linear Regression using Scikit-Learn
    - Implements Backward Elimination using Statsmodels OLS to find the most significant features
    - Evaluates model performance via R-squared and Bias-Variance analysis
"""

# =========================================
# Import Required Libraries
# =========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

# =========================================
# Load Dataset
# =========================================
path = os.path.dirname(__file__)
dataset = pd.read_csv(os.path.join(path, "Investment.csv"))

# Independent variables (features)
# Columns: DigitalMarketing, Promotion, Research, State
X = dataset.iloc[:, :-1]

# Dependent variable (target / label)
# Column: Profit
y = dataset.iloc[:, 4]

# Preview the dataset
print("--- Dataset Preview ---")
print(dataset.head())

# =========================================
# Data Preprocessing: Categorical Encoding
# =========================================
# Convert 'State' to dummy variables. 
# Statsmodels requires numeric inputs for OLS.
X = pd.get_dummies(X, dtype=int)

# =========================================
# Train-Test Split
# =========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# =========================================
# Model Training – Multiple Linear Regression
# =========================================
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# =========================================
# Prediction on Test Data
# =========================================
y_pred = regressor.predict(X_test)

# Display Intercept and Coefficients
print("\n--- Model Parameters ---")
print("Model Intercept (b0):", regressor.intercept_)
print("Model Coefficients (b1, b2, ...):", regressor.coef_)

# =========================================
# Backward Elimination (Building Optimal Model)
# =========================================
# Statsmodels OLS requires a column of constants (1s) to represent the intercept b0.
# The original script used a constant of 42467, but 1.0 is the standard mathematical approach.
X = sm.add_constant(X)

# Backward Elimination Strategy:
# 1. Select a Significance Level (SL = 0.05)
# 2. Fit the model with all predictors
# 3. If P-value > SL, remove the predictor with highest P-value and refit.

print("\n--- Backward Elimination: Iteration 1 (All Features) ---")
# Indices: 0-Const, 1-DigitalMarketing, 2-Promotion, 3-Research, 4-State_Bangalore, 5-State_Chennai, 6-State_Hyderabad
X_opt = X.iloc[:, [0, 1, 2, 3, 4, 5, 6]].values.astype(float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

# Removing State_Hyderabad (Index 6)
print("\n--- Backward Elimination: Iteration 2 (Removing State_Hyderabad) ---")
X_opt = X.iloc[:, [0, 1, 2, 3, 4, 5]].values.astype(float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print("Max P-value for Iteration 2:", max(regressor_OLS.pvalues))

# Removing State_Bangalore (Index 4)
print("\n--- Backward Elimination: Iteration 3 (Removing State_Bangalore) ---")
X_opt = X.iloc[:, [0, 1, 2, 3, 5]].values.astype(float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()

# Removing State_Chennai (Index 5)
print("\n--- Backward Elimination: Iteration 4 (Removing State_Chennai) ---")
X_opt = X.iloc[:, [0, 1, 2, 3]].values.astype(float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()

# Removing Promotion (Index 2)
print("\n--- Backward Elimination: Iteration 5 (Removing Promotion) ---")
X_opt = X.iloc[:, [0, 1, 3]].values.astype(float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()

# Removing Research (Index 3)
print("\n--- Backward Elimination: Iteration 6 (Removing Research) ---")
X_opt = X.iloc[:, [0, 1]].values.astype(float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()

# Final result showing DigitalMarketing is the most significant
print("\n--- Final Optimized Model Summary ---")
print(regressor_OLS.summary())

# =========================================
# Bias – Variance Analysis
# =========================================
training_score = regressor.score(X_train, y_train)
testing_score = regressor.score(X_test, y_test)

print("\n--- Model Evaluation ---")
print(f"Bias (Training Accuracy - R2): {training_score:.4f}")
print(f"Variance (Testing Accuracy - R2): {testing_score:.4f}")

# =========================================
# Visualization & Saving Model
# =========================================
# Plotting Actual vs Predicted Values for Test Set
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, color='red', label='Actual Profit', marker='o')
plt.scatter(range(len(y_pred)), y_pred, color='blue', label='Predicted Profit', marker='x')
plt.title('Investment Profit: Actual vs Predicted (Test Set)')
plt.xlabel('Sample Index')
plt.ylabel('Profit')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
# plt.show() # Uncomment to display the plot locally

# Saving the trained model for future use
import joblib
model_filename = os.path.join(current_dir, 'investment_profit_model.pkl')
joblib.dump(regressor, model_filename)

print(f"\nModel saved successfully as: {model_filename}")
print("\nOptimization Complete. DigitalMarketing (R&D) identified as the primary predictor of Profit.")