"""
File Name   : random_forest_classification_model.py
Purpose     : Binary Classification using Random Forest (Ensemble Learning)
Dataset     : logistic-classification.csv
Author      : Venkatesh Singamsetty
Description :
    - Loads social media advertisement data
    - Implements Random Forest Classifier (Ensemble of Decision Trees)
    - Performs Feature Scaling (Optional but good for comparison consistency)
    - Optimizes hyperparameters: n_estimators, max_depth, criterion
    - Evaluates performance via Confusion Matrix, Accuracy, and Bias-Variance analysis
    - Persists the trained model and scaler for deployment
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
from sklearn.ensemble import RandomForestClassifier
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
# Random Forest is not distance-based, but scaling is good for consistency.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================================
# Model Training – Random Forest Classifier
# =========================================
# n_estimators: Number of trees in the forest
# criterion: 'entropy' for information gain
# max_depth: Controls overfitting
classifier = RandomForestClassifier(n_estimators=33, max_depth=5, criterion='entropy', max_features=2, random_state=0)
classifier.fit(X_train, y_train)

# =========================================
# Model Evaluation
# =========================================
y_pred = classifier.predict(X_test)

print("\n--- Model Evaluation ---")
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print(f"Accuracy Score: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Bias - Variance Analysis (Overfitting check)
training_accuracy = classifier.score(X_train, y_train)
testing_accuracy = classifier.score(X_test, y_test)

print("--- Bias & Variance ---")
print(f"Training Accuracy (Bias Check): {training_accuracy:.4f}")
print(f"Testing Accuracy (Variance Check): {testing_accuracy:.4f}")

# =========================================
# Model Persistence
# =========================================
# Save the model and scaler for future deployment
model_file = os.path.join(current_dir, "random_forest_model.joblib")
scaler_file = os.path.join(current_dir, "scaler_rf.joblib")

joblib.dump(classifier, model_file)
joblib.dump(scaler, scaler_file)

print(f"\nModel and Scaler saved successfully in: {current_dir}")
print("Random Forest classification workflow complete.")
