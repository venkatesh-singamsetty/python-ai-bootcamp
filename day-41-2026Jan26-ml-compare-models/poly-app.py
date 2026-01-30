import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

lin_model_pred = lin_reg.predict([[6.5]])
print(lin_model_pred)

from sklearn.preprocessing import PolynomialFeatures
# poly_reg = PolynomialFeatures()
# poly_reg = PolynomialFeatures(degree = 3)
# poly_reg = PolynomialFeatures(degree = 4)
# poly_reg = PolynomialFeatures(degree = 5)
# poly_reg = PolynomialFeatures(degree = 6)
# poly_reg = PolynomialFeatures(degree = 7)
poly_reg = PolynomialFeatures(degree = 5)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth of Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_model_pred)

# svr model
from sklearn.svm import SVR
# svr_reg = SVR()
svr_reg = SVR(kernel='poly', degree=5)
svr_reg.fit(X, y)

svr_model_pred = svr_reg.predict([[6.5]])
print(svr_model_pred)

# knn regression model 
from sklearn.neighbors import KNeighborsRegressor
# knn_reg = KNeighborsRegressor()
# knn_reg = KNeighborsRegressor(n_neighbors=3, weights='distance')
knn_reg = KNeighborsRegressor(n_neighbors=4)
knn_reg.fit(X, y)

knn_model_pred = knn_reg.predict([[6.5]])
print(knn_model_pred)

# dtr model
from sklearn.tree import DecisionTreeRegressor
dtr_reg = DecisionTreeRegressor()
#dtr_reg = DecisionTreeRegressor(criterion='absolute_error', splitter='random')
dtr_reg.fit(X, y)

dtr_model_pred = dtr_reg.predict([[6.5]])
print(dtr_model_pred)


# rfr model
from sklearn.ensemble import RandomForestRegressor
# rfr_reg = RandomForestRegressor()
rfr_reg = RandomForestRegressor(random_state = 0)
rfr_reg.fit(X, y)

rfr_model_pred = rfr_reg.predict([[6.5]])
print(rfr_model_pred)
