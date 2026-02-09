"""
File Name   : kmeans_clustering_model.py
Purpose     : Customer Segmentation using K-Means Clustering
Dataset     : Mall_Customers.csv
Author      : Venkatesh Singamsetty
Description :
    - Loads customer demographic and spending data
    - Uses the Elbow Method to find the optimal number of clusters
    - Trains the K-Means model with k-means++ initialization
    - Visualizes the clusters and identifies centroids
    - Saves the clustered dataset for targeted marketing analysis
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
from sklearn.cluster import KMeans

# =========================================
# Environment Setup & Data Loading
# =========================================
current_dir = os.path.dirname(__file__)
dataset_name = "Mall_Customers.csv"
dataset_path = os.path.join(current_dir, dataset_name)

# Guard clause for dataset existence
if not os.path.exists(dataset_path):
    print(f"Error: Dataset '{dataset_name}' not found in {current_dir}")
    sys.exit(1)

dataset = pd.read_csv(dataset_path)

# Independent variables: Annual Income (k$) and Spending Score (1-100)
X = dataset.iloc[:, [3, 4]].values

print("--- Dataset Overview ---")
print(dataset.head())

# =========================================
# Finding Optimal Clusters via Elbow Method
# =========================================
print("\n--- Applying Elbow Method... ---")
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('The Elbow Method for Optimal K')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.grid(True, alpha=0.3)
# plt.show() # Uncomment to view the elbow plot
print("Tip: The 'elbow' point (where the drop slows down) indicates the optimal number of clusters.")

# =========================================
# Training K-Means Model
# =========================================
# Based on the elbow plot, 5 clusters is ideal for this dataset
n_clusters = 5
print(f"\n--- Training K-Means Classifier (k={n_clusters}) ---")

kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Add cluster labels to the original dataframe
dataset['Cluster_Label'] = y_kmeans

# =========================================
# Visualizing the Clusters
# =========================================
plt.figure(figsize=(10, 7))
colors = ['red', 'blue', 'green', 'cyan', 'magenta']

for i in range(n_clusters):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], 
                s=100, c=colors[i], label=f'Cluster {i+1}')

# Plotting the centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            s=300, c='yellow', label='Centroids', edgecolors='black')

plt.title('Customer Segments (K-Means Clustering)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
# plt.show() # Uncomment to show the cluster scatter plot

# =========================================
# Persistence: Saving the Model & Results
# =========================================
model_file = os.path.join(current_dir, "kmeans_model.joblib")
output_file = os.path.join(current_dir, "Mall_Customers_KMeans_Clustered.csv")

joblib.dump(kmeans, model_file)
dataset.to_csv(output_file, index=False)

print(f"\nModel saved successfully as: {model_file}")
print(f"Results saved to: {output_file}")
print("K-Means workflow complete.")
