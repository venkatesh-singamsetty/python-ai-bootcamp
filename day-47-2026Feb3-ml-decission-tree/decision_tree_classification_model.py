"""
File Name   : decision_tree_classification_model.py
Purpose     : Binary Classification using Decision Tree
Dataset     : logistic-classification.csv
Author      : Venkatesh Singamsetty
Description :
    - Loads social media advertisement data
    - Performs Feature Scaling (Optional for Decision Trees, but kept for consistency)
    - Trains a Decision Tree Classifier with Entropy criterion
    - Evaluates performance using Confusion Matrix, Accuracy, and ROC-AUC
    - Visualizes the ROC Curve
    - Analyzes Bias and Variance
    - Persists the model and scaler for future use
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
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score, roc_curve

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
# Note: Decision Trees are scale-invariant, but scaling is done for consistency 
# and if you decide to compare with distance-based models (like KNN/SVM).
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================================
# Model Training – Decision Tree Classifier
# =========================================
# Using 'entropy' for Information Gain and limiting depth to prevent overfitting
classifier = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=0)
classifier.fit(X_train, y_train)

# =========================================
# Model Evaluation
# =========================================
y_pred = classifier.predict(X_test)
y_pred_prob = classifier.predict_proba(X_test)[:, 1]

print("\n--- Model Evaluation ---")
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_pred_prob)

print("Confusion Matrix:\n", cm)
print(f"Accuracy Score: {accuracy:.4f}")
print(f"ROC-AUC Score: {auc_score:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Bias - Variance Analysis
training_accuracy = classifier.score(X_train, y_train)
testing_accuracy = classifier.score(X_test, y_test)

print("--- Bias & Variance Analysis ---")
print(f"Training Accuracy (Bias Check): {training_accuracy:.4f}")
print(f"Testing Accuracy (Variance Check): {testing_accuracy:.4f}")

# =========================================
# Visualizing the ROC Curve
# =========================================
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'Decision Tree (AUC = {auc_score:.2f})', color='darkorange', lw=2)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')  # Random classifier line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.grid(alpha=0.3)
# plt.show() # Uncomment to show plot

# =========================================
# Model Persistence
# =========================================
model_file = os.path.join(current_dir, "decision_tree_model.joblib")
scaler_file = os.path.join(current_dir, "scaler_dt.joblib")

joblib.dump(classifier, model_file)
joblib.dump(scaler, scaler_file)

print(f"\nModel and Scaler saved successfully in: {current_dir}")
print("Decision Tree classification workflow complete.")
