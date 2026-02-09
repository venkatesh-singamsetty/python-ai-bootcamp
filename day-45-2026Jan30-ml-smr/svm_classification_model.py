"""
File Name   : svm_classification_model.py
Purpose     : Binary Classification using Support Vector Machine (SVM)
Dataset     : logistic-classification.csv
Algorithm   : SVC with RBF Kernel
Author      : Venkatesh Singamsetty
Description :
    - Loads advertisement data and separates features
    - Performs Feature Scaling (StandardScaler) which is essential for SVM
    - Trains an SVM model with a Radial Basis Function (RBF) kernel
    - Evaluates performance via Confusion Matrix, Accuracy, and Classification Report
    - Analyzes Bias and Variance for overfitting check
    - Persists the trained model and scaler for future deployment
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
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
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
# Feature Scaling (Crucial for SVM)
# =========================================
# SVM tries to maximize the margin between classes. 
# Features on different scales (Age vs Salary) can severely bias the model.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================================
# Model Training – SVM Classifier
# =========================================
# Using 'rbf' kernel for non-linear boundaries. 
# 'gamma=scale' is the modern standard for kernel coefficient.
svm_classifier = SVC(kernel='rbf', gamma='scale', random_state=0)
svm_classifier.fit(X_train, y_train)

# =========================================
# Model Evaluation
# =========================================
y_pred = svm_classifier.predict(X_test)

print("\n--- Model Evaluation ---")
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print(f"Accuracy Score: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Bias - Variance Analysis
training_accuracy = svm_classifier.score(X_train, y_train)
testing_accuracy = svm_classifier.score(X_test, y_test)

print("--- Bias & Variance Analysis ---")
print(f"Training Accuracy (Bias Check): {training_accuracy:.4f}")
print(f"Testing Accuracy (Variance Check): {testing_accuracy:.4f}")

# =========================================
# Model Persistence
# =========================================
model_file = os.path.join(current_dir, "svm_rbf_model.joblib")
scaler_file = os.path.join(current_dir, "scaler_std.joblib")

joblib.dump(svm_classifier, model_file)
joblib.dump(scaler, scaler_file)

print(f"\nModel and Scaler saved successfully in: {current_dir}")
print("SVM classification workflow complete.")
