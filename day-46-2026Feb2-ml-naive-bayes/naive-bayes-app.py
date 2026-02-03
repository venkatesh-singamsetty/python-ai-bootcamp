# Naive Bayes

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
# Using absolute path to ensure it works regardless of the current working directory
dataset = pd.read_csv(r"/Users/venkat/workspace/gitRepos/python-genAi-agenticAI/day-46-2026Feb2-ml-naive-bayes/logistic-classification.csv")

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# Split the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

from sklearn.preprocessing import Normalizer
sc = Normalizer()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Naive Bayes model on the training set
# from sklearn.naive_bayes import GaussianNB
# classifier = GaussianNB()
# classifier.fit(X_train, y_train)

# Training the Naive Bayes model on the training set
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Predicting the test set results
y_pred = classifier.predict(X_test)

# Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Accuracy Score
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)
