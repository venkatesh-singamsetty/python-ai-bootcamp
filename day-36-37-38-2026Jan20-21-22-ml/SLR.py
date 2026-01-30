import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
print(dataset.head())

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

plt.scatter(x_test, y_test, color='red')
plt.plot(x_test, regressor.predict(x_test), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print(regressor)

m_slope = regressor.coef_
print(m_slope)

c_intercept = regressor.intercept_
print(c_intercept)

emp_15 = m_slope * 15 + c_intercept
print(emp_15)

emp_20 = m_slope * 20 + c_intercept
print(emp_20)

bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)

dataset.mean()

print(dataset['Salary'].mean())
print(dataset['Salary'].median())
print(dataset['Salary'].mode())

print(dataset['Salary'].var())

dataset.std()
dataset['Salary'].std()


from scipy.stats import variation
print(variation(dataset.values))
print(variation(dataset['Salary']))

dataset.corr()
print(dataset['Salary'].corr(dataset['YearsExperience']))

dataset.skew()
print(dataset['Salary'].skew())

dataset.sem()

from scipy.stats import stats
dataset.apply(stats.zscore)

stats.zscore(dataset['Salary'])

# ssr
y_mean = np.mean(y)
SSR = np.sum((y_pred - y_mean) ** 2)
print(SSR)

# sse
y = y[0:6]
SSE = np.sum((y - y_pred) ** 2)
print(SSE)

# sst
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values - mean_total) ** 2)
print(SST)

# r2
r_square = 1 - SSR/SST
print(r_square)

# bias
bias = regressor.score(x_train, y_train)
print(bias)

# variance
variance = regressor.score(x_test, y_test)
print(variance) 

from sklearn.metrics import mean_squared_error, mean_absolute_error
import pickle

train_mse = mean_squared_error(y_train, regressor.predict(x_train))
test_mse = mean_squared_error(y_test, y_pred)
train_mae = mean_absolute_error(y_train, regressor.predict(x_train))

print(f"Training Score (R^2): {bias:.2f}")
print(f"Test Score (R^2): {variance:.2f}")
print(f"Training MSE: {train_mse:.2f}")
print(f"Test MSE: {test_mse:.2f}")

# Save the trained model to disk
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print(f"Model has been pickled and saved as linear_regression_model.pkl")

import os
print(os.getcwd())
