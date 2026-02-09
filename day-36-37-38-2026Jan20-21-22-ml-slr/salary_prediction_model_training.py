
# ==========================================
# 1. Load Dataset
# ==========================================
import pandas as pd
import os
import joblib

path = os.path.dirname(__file__)
dataset = pd.read_csv(os.path.join(path, "Salary_Data.csv"))

# ==========================================
# 2. Data Preprocessing
# ==========================================
from sklearn.model_selection import train_test_split

# X = Independent Variable (YearsExperience) - Reshaped as 2D array
X = dataset.iloc[:, :-1].values
# y = Dependent Variable (Salary) - 1D array
y = dataset.iloc[:, 1].values 

# Split the dataset into training and testing sets (80-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# ==========================================
# 3. Model Training
# ==========================================
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# ==========================================
# 4. Prediction & Evaluation
# ==========================================
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

y_pred = regressor.predict(X_test)
y_train_pred = regressor.predict(X_train)

# Comparison Dataframe
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\n--- Predictions vs Actual ---")
print(comparison)

# Performance Metrics
# 1. R-Squared (R²): Coefficient of Determination
#    - Represents the proportion of variance in the dependent variable (Salary) explained by the independent variable (Experience).
#    - Range: 0 to 1 (closer to 1 is better).
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_pred)

# 2. Mean Squared Error (MSE)
#    - The average of the squared differences between Predicted and Actual values.
#    - Penalizes larger errors more significantly than smaller ones.
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_pred)

# 3. Root Mean Squared Error (RMSE)
#    - The square root of MSE.
#    - Returns the error to the original units (e.g., Dollars), making it easier to interpret.
train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

# 4. Mean Absolute Error (MAE)
#    - The average of the absolute differences between Predicted and Actual values.
#    - Gives a linear representation of error magnitude.
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_pred)

print("\n--- Model Performance ---")
print(f"Training R² Score: {train_r2:.2f}")
print(f"Testing R² Score: {test_r2:.2f}")
print(f"Training MSE: {train_mse:.2f}")
print(f"Testing MSE: {test_mse:.2f}")
print(f"Training RMSE: {train_rmse:.2f}")
print(f"Testing RMSE: {test_rmse:.2f}")
print(f"Training MAE: {train_mae:.2f}")
print(f"Testing MAE: {test_mae:.2f}")

# Manual Prediction Examples
y_12 = regressor.predict([[12]])
y_20 = regressor.predict([[20]])
print(f"\nPredicted salary for 12 years: ${y_12[0]:,.2f}")
print(f"Predicted salary for 20 years: ${y_20[0]:,.2f}")

# ==========================================
# 5. Visualization
# ==========================================
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))

# Plot Training Selection
plt.subplot(1, 2, 1)
# Visualize the Training set results
# Scatter plot shows actual data points (Red)
plt.scatter(X_train, y_train, color='red', label='Actual Data')
# Line plot shows the regression line (Blue) - predictions on training data
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Regression Line')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()

# Plot Test Selection
plt.subplot(1, 2, 2)
# Visualize the Test set results
plt.scatter(X_test, y_test, color='red', label='Actual Data')
# Regression line is the same (blue line) derived from training data
# Why use the Training Regression Line here?
# We want to see how well the model (learned from training data) fits the NEW (test) data.
# The blue line represents the relationship learned during training (y = mx + c).
# If we recalculated the line using Test Data, we would be training a new model, not testing the old one.
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Regression Line')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()

plt.tight_layout()
plt.show()

# ==========================================
# 6. Statistical Summary (OLS)
# ==========================================
from statsmodels.api import OLS

# OLS (Ordinary Least Squares) Regression Analysis
# This provides a detailed statistical summary of the regression model.
# Insights include:
# - R-squared: How well the independent variable explains the variance in the dependent variable.
# - Prob (F-statistic): Significance of the overall model.
# - Coefficients (coef): The impact of independent variables on the dependent variable.
# - P>|t|: The p-value for each coefficient (helps in feature selection).
print("\n--- OLS Regression Results ---")
print(OLS(y_train, X_train).fit().summary())

# ==========================================
# 7. Save Model
# ==========================================
# Serialization: Save the trained model for the Streamlit app
filename = os.path.join(path, "linear_regression_model.joblib")
joblib.dump(regressor, filename)
print(f"\nModel has been saved to: {filename}")
