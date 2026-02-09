"""
File Name   : naive_bayes_classification_model.py
Purpose     : Binary Classification using Naive Bayes
Dataset     : logistic-classification.csv
Author      : Venkatesh Singamsetty
Description :
    - Performs Feature Scaling (Standardization vs Normalization)
    - Compares Naive Bayes variants (Gaussian vs Multinomial)
    - Evaluates performance using Confusion Matrix and Accuracy Score
    - Analyzes Bias and Variance
    - Saves the trained model for future use
"""

# =========================================
# Import Required Libraries
# =========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# =========================================
# Data Loading
# =========================================
path = os.path.dirname(__file__)
dataset = pd.read_csv(os.path.join(path, "logistic-classification.csv"))

# Independent variables: Age (index 2) and EstimatedSalary (index 3)
X = dataset.iloc[:, [2, 3]].values

# Dependent variable: Purchased (index 4 / -1)
y = dataset.iloc[:, -1].values

print("--- Dataset Overview ---")
print(dataset.head())

# =========================================
# Train-Test Split
# =========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# =========================================
# Feature Scaling
# =========================================
# NOTE: Naive Bayes performance can vary significantly with scaling.
# GaussianNB typically works best with StandardScaler.
# MultinomialNB requires non-negative values (Normalization is one way to ensure this).

# Option 1: Standardization (Best for GaussianNB)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Option 2: Normalization (Alternative)
norm = Normalizer()
X_train_norm = norm.fit_transform(X_train)
X_test_norm = norm.transform(X_test)

# =========================================
# Model Training – Gaussian Naive Bayes (Recommended)
# =========================================
print("\n--- Training Gaussian Naive Bayes ---")
classifier = GaussianNB()
classifier.fit(X_train_std, y_train)

# =========================================
# Model Evaluation
# =========================================
y_pred = classifier.predict(X_test_std)

print("\n--- Model Evaluation Results ---")
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print(f"Accuracy Score: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Bias - Variance Analysis
training_score = classifier.score(X_train_std, y_train)
testing_score = classifier.score(X_test_std, y_test)

print("--- Bias & Variance Analysis ---")
print(f"Training Accuracy (Bias Check): {training_score:.4f}")
print(f"Testing Accuracy (Variance Check): {testing_score:.4f}")

# =========================================
# Model Persistence
# =========================================
model_file = os.path.join(current_dir, "naive_bayes_model.joblib")
scaler_file = os.path.join(current_dir, "scaler_std.joblib")

joblib.dump(classifier, model_file)
joblib.dump(sc, scaler_file)

print(f"\nModel and Scaler saved successfully in: {current_dir}")
print("Workflow complete.")
