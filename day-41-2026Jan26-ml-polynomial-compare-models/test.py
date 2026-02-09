# =========================================
# Multiple Regression Models Comparison
# =========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# Load Dataset
# -----------------------------------------
dataset = pd.read_csv("emp_sal.csv")

# Independent variable (Position Level)
X = dataset.iloc[:, 1:2].values   # 2D array for sklearn

# Dependent variable (Salary)
y = dataset.iloc[:, 2].values

# -----------------------------------------
# 1. Linear Regression
# -----------------------------------------
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Visualization
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

print("Linear Regression Prediction (6.5):",
      lin_reg.predict([[6.5]]))

# -----------------------------------------
# 2. Polynomial Regression
# -----------------------------------------
from sklearn.preprocessing import PolynomialFeatures
# poly_reg = PolynomialFeatures()
# poly_reg = PolynomialFeatures(degree = 3)
# poly_reg = PolynomialFeatures(degree = 4)
# poly_reg = PolynomialFeatures(degree = 5)
# poly_reg = PolynomialFeatures(degree = 6)
# poly_reg = PolynomialFeatures(degree = 7)
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)

poly_lin_reg = LinearRegression()
poly_lin_reg.fit(X_poly, y)

# Visualization
plt.scatter(X, y, color='red')
plt.plot(X, poly_lin_reg.predict(X_poly), color='blue')
plt.title('Polynomial Regression (Degree 5)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

print("Polynomial Regression Prediction (6.5):",
      poly_lin_reg.predict(poly_reg.transform([[6.5]])))

# -----------------------------------------
# 3. Support Vector Regression (SVR)
# -----------------------------------------
from sklearn.svm import SVR
# svr_reg = SVR()
svr_reg = SVR(kernel='poly', degree=5)
svr_reg.fit(X, y)

print("SVR Prediction (6.5):",
      svr_reg.predict([[6.5]]))

# -----------------------------------------
# 4. K-Nearest Neighbors Regression
# -----------------------------------------
from sklearn.neighbors import KNeighborsRegressor
# knn_reg = KNeighborsRegressor()
# knn_reg = KNeighborsRegressor(n_neighbors=3, weights='distance')
knn_reg = KNeighborsRegressor(n_neighbors=4)
knn_reg.fit(X, y)

print("KNN Prediction (6.5):",
      knn_reg.predict([[6.5]]))

# -----------------------------------------
# 5. Decision Tree Regression
# -----------------------------------------
from sklearn.tree import DecisionTreeRegressor

dtr_reg = DecisionTreeRegressor(random_state=0)
dtr_reg.fit(X, y)

print("Decision Tree Prediction (6.5):",
      dtr_reg.predict([[6.5]]))

# -----------------------------------------
# 6. Random Forest Regression
# -----------------------------------------
from sklearn.ensemble import RandomForestRegressor

rfr_reg = RandomForestRegressor(n_estimators=100, random_state=0)
rfr_reg.fit(X, y)

print("Random Forest Prediction (6.5):",
      rfr_reg.predict([[6.5]]))
