"""
File Name   : logistic_classification_knn_model.py
Purpose     : Binary Classification using K-Nearest Neighbors (KNN)
Dataset     : logistic-classification.csv
Author      : Venkatesh Singamsetty
Description :
    - Loads social media advertisement data
    - Performs Feature Scaling (Standardization) which is mandatory for KNN
    - Trains a KNN model using the Minkowski metric (Euclidean distance)
    - Evaluates performance via Confusion Matrix and Accuracy
    - Analyzes Bias and Variance
    - Generates predictions for unseen data from 'final1-sample.csv'
    - Saves the trained model and results for deployment
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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# =========================================
# Data Loading
# =========================================
path = os.path.dirname(__file__)
dataset = pd.read_csv(os.path.join(path, "logistic-classification.csv"))
future_data_path = os.path.join(path, "final1-sample.csv")

# Independent variables: Age (index 2) and EstimatedSalary (index 3)
X = dataset.iloc[:, [2, 3]].values

# Dependent variable: Purchased (index 4 / -1)
y = dataset.iloc[:, -1].values

print("--- Dataset Overview ---")
print(dataset.head())

# =========================================
# Train-Test Split
# =========================================
# 80-20 split is standard for this dataset size
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# =========================================
# Feature Scaling (Crucial for Distance-based Algorithms)
# =========================================
# KNN relies on Euclidean distance; without scaling, Salary would dominate Age
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================================
# Model Training – KNN Classifier
# =========================================
# Using 5 neighbors and Euclidean distance (p=2)
knn_classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn_classifier.fit(X_train, y_train)

# =========================================
# Model Evaluation
# =========================================
y_pred = knn_classifier.predict(X_test)

print("\n--- Model Evaluation ---")
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print(f"Accuracy Score: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Bias-Variance Analysis
training_score = knn_classifier.score(X_train, y_train)
testing_score = knn_classifier.score(X_test, y_test)

print("--- Bias & Variance ---")
print(f"Training Accuracy (Bias Check): {training_score:.4f}")
print(f"Testing Accuracy (Variance Check): {testing_score:.4f}")

# =========================================
# Visualizing Results (Optional Setup)
# =========================================
def plot_decision_boundary(X_set, y_set, title):
    from matplotlib.colors import ListedColormap
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                         np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
    plt.contourf(X1, X2, knn_classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c = ListedColormap(('red', 'green'))[i], label = j)
    plt.title(title)
    plt.xlabel('Age (Scaled)')
    plt.ylabel('Estimated Salary (Scaled)')
    plt.legend()
    # plt.show() # Uncomment to show plots

# Note: Decision boundary plotting can be slow; uncomment if needed for reports.
# plt.figure(figsize=(10,5))
# plot_decision_boundary(X_test, y_test, 'KNN (Test set) Decision Boundary')

# =========================================
# Persistence: Saving the Model & Scaler
# =========================================
model_file = os.path.join(current_dir, "knn_model.joblib")
scaler_file = os.path.join(current_dir, "scaler.joblib")

joblib.dump(knn_classifier, model_file)
joblib.dump(scaler, scaler_file)
print(f"\nModel and Scaler saved successfully.")

# =========================================
# Future Prediction Workflow
# =========================================
if os.path.exists(future_data_path):
    print("\n--- Running Future Predictions ---")
    future_data = pd.read_csv(future_data_path)
    output_df = future_data.copy()

    # Selecting Age and Salary for the new data (adjust indices if needed)
    X_future = future_data.iloc[:, [3, 4]].values
    
    # Scale new data using the SAME scaler from training
    X_future_scaled = scaler.transform(X_future)
    
    # Generate predictions
    output_df['Purchased_Prediction'] = knn_classifier.predict(X_future_scaled)
    
    # Save output
    output_file = os.path.join(current_dir, "final_predictions.csv")
    output_df.to_csv(output_file, index=False)
    print(f"Predictions saved to: {output_file}")
else:
    print(f"\nNote: Future data file {future_data_path} not found. Skipping prediction step.")

print("\nClassification workflow complete.")
