"""
File Name   : employee_salary_regression_models.py
Purpose     : Multiple Regression Models Comparison for Salary Prediction
Dataset     : emp_sal.csv
Author      : Venkatesh Singamsetty
Description :
    - Compares Linear, Polynomial, SVR, KNN, DT, and RF regression.
    - Saves models using joblib for deployment.
"""

import numpy as np
import pandas as pd
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
current_dir = os.path.dirname(__file__)
dataset_path = os.path.join(current_dir, "emp_sal.csv")
dataset = pd.read_csv(dataset_path)

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# 1. Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# 2. Polynomial Regression (Degree 5)
poly_feat = PolynomialFeatures(degree=5)
X_poly = poly_feat.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

# 3. Support Vector Regression (SVR)
# SVR requires scaling for better results
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).ravel()

svr_reg = SVR(kernel='poly', degree=5)
svr_reg.fit(X_scaled, y_scaled)

# 4. K-Nearest Neighbors Regression
knn_reg = KNeighborsRegressor(n_neighbors=4)
knn_reg.fit(X, y)

# 5. Decision Tree Regression
dt_reg = DecisionTreeRegressor(random_state=0)
dt_reg.fit(X, y)

# 6. Random Forest Regression
rf_reg = RandomForestRegressor(n_estimators=100, random_state=0)
rf_reg.fit(X, y)

# Persistence
joblib.dump(lin_reg, os.path.join(current_dir, "linear_model.joblib"))
joblib.dump(poly_reg, os.path.join(current_dir, "poly_model.joblib"))
joblib.dump(poly_feat, os.path.join(current_dir, "poly_feat.joblib"))
joblib.dump(svr_reg, os.path.join(current_dir, "svr_model.joblib"))
joblib.dump(scaler_X, os.path.join(current_dir, "scaler_X.joblib"))
joblib.dump(scaler_y, os.path.join(current_dir, "scaler_y.joblib"))
joblib.dump(knn_reg, os.path.join(current_dir, "knn_model.joblib"))
joblib.dump(dt_reg, os.path.join(current_dir, "dt_model.joblib"))
joblib.dump(rf_reg, os.path.join(current_dir, "rf_model.joblib"))

print(f"All 6 models and scalers saved in: {current_dir}")
