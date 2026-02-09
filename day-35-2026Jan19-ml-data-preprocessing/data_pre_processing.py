# Data Preprocessing Template

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
import os
dataset_path = os.path.join(os.path.dirname(__file__), 'Data.csv')
dataset = pd.read_csv(dataset_path)
print(dataset.head()) # Verify the first few rows

# Separating the data into Independent Variables (Matrix of Features) and Dependent Variable (Vector of Response)
# x = Features (all columns except the last one)
# y = Target Label (the last column)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
from sklearn.impute import SimpleImputer
# Strategies: 'mean' (default), 'median', 'most_frequent', 'constant'
# imputer = SimpleImputer() # Default is mean
# imputer = SimpleImputer(strategy="median")
# imputer = SimpleImputer(strategy="mode") # 'mode' is not a valid strategy string in newer sklearn, use 'most_frequent'
imputer = SimpleImputer(strategy="most_frequent")

# Apply imputer to columns with missing data (assuming columns 1 and 2 index-wise here)
# imputer.fit(data): Learns the parameters (e.g., mean, median, most frequent) from the data columns.
imputer = imputer.fit(x[:, 1:3])

# imputer.transform(data): Uses the learned parameters to replace missing values (NaNs) in the data.
x[:, 1:3] = imputer.transform(x[:, 1:3])

# Encoding categorical data
# Encoding the Independent Variable (e.g., Country column at index 0)
from sklearn.preprocessing import LabelEncoder
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

# Encoding the Dependent Variable (e.g., Purchased column)
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
# test_size = 0.2 means 20% of data is for testing, 80% for training
# random_state = 0 ensures reproducibility of the split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, random_state=0)
