"""
File Name   : xgboost_classification_model.py
Purpose     : Binary Classification using XGBoost (Extreme Gradient Boosting)
Dataset     : Churn_Modelling.csv
Author      : Venkatesh Singamsetty
Description :
    - Loads customer churn data for a bank
    - Handles categorical data: Label Encoding for Gender and One-Hot Encoding for Geography
    - Implements XGBoost Classifier for high-performance prediction
    - Performs 5-Fold Cross Validation to ensure model stability
    - Evaluates performance via Confusion Matrix, Accuracy, and Bias-Variance analysis
    - Persists the trained model and preprocessing transformers for deployment
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
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# =========================================
# Environment Setup & Data Loading
# =========================================
current_dir = os.path.dirname(__file__)
dataset_name = "Churn_Modelling.csv"
dataset_path = os.path.join(current_dir, dataset_name)

# Guard clause for dataset existence
if not os.path.exists(dataset_path):
    print(f"Error: Dataset '{dataset_name}' not found in {current_dir}")
    sys.exit(1)

dataset = pd.read_csv(dataset_path)

# Independent variables: From CreditScore (index 3) to EstimatedSalary (index -2)
X = dataset.iloc[:, 3:-1].values

# Dependent variable: Exited (index -1)
y = dataset.iloc[:, -1].values

print("--- Dataset Loaded Successfully ---")
print(f"Dataset Shape: {dataset.shape}")
print(dataset.head())

# =========================================
# Categorical Data Encoding
# =========================================
# 1. Label Encoding "Gender" (X index 2)
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])
print("\nGender encoded successfully.")

# 2. One-Hot Encoding "Geography" (X index 1)
# Using ColumnTransformer to apply OneHotEncoder to Geography and passthrough others
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print("Geography One-Hot encoded successfully.")

# =========================================
# Train-Test Split
# =========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# =========================================
# Model Training – XGBoost Classifier
# =========================================
print("\n--- Training XGBoost Classifier ---")
# XGBoost is an optimized distributed gradient boosting library.
# eval_metric='logloss' helps monitor performance during training.
classifier = XGBClassifier(random_state=0, eval_metric='logloss')
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

print("--- Bias & Variance Analysis ---")
print(f"Training Accuracy (Bias Check): {training_accuracy:.4f}")
print(f"Testing Accuracy (Variance Check): {testing_accuracy:.4f}")

# =========================================
# K-Fold Cross Validation
# =========================================
# Ensuring the model generalizes well across different subsets of data
print("\n--- Applying 5-Fold Cross Validation ---")
accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=5)
print("Standard Mean Accuracy: {:.2f} %".format(accuracies.mean() * 100))
print("Standard Deviation: {:.2f} %".format(accuracies.std() * 100))

# =========================================
# Model Persistence
# =========================================
# Save the model and encoders for future use
model_file = os.path.join(current_dir, "xgboost_churn_model.joblib")
preprocessor_file = os.path.join(current_dir, "preprocessor_ct.joblib")
label_encoder_file = os.path.join(current_dir, "label_encoder_gender.joblib")

joblib.dump(classifier, model_file)
joblib.dump(ct, preprocessor_file)
joblib.dump(le, label_encoder_file)

print(f"\nModel and Preprocessor saved successfully in: {current_dir}")
print("XGBoost classification workflow complete.")
