"""
File Name   : hierarchical_clustering_model.py
Purpose     : Customer Segmentation using Hierarchical Clustering
Dataset     : Mall_Customers.csv
Author      : Venkatesh Singamsetty
Description :
    - Loads customer data (Annual Income and Spending Score)
    - Uses a Dendrogram to determine the optimal number of clusters
    - Fits the Agglomerative Hierarchical Clustering model
    - Visualizes the resulting clusters
    - Saves the clustered dataset for business analysis
"""

# =========================================
# Import Required Libraries
# =========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

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

# Selecting features: Annual Income (k$) and Spending Score (1-100)
# Usually columns at index 3 and 4
X = dataset.iloc[:, [3, 4]].values

print("--- Dataset Overview ---")
print(dataset.head())

# =========================================
# Finding Optimal Clusters via Dendrogram
# =========================================
print("\n--- Generating Dendrogram... ---")
plt.figure(figsize=(12, 8))
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram for Optimal Cluster Selection')
plt.xlabel('Customers (Data Points)')
plt.ylabel('Euclidean distances')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show() # Uncomment to view the dendrogram to identify the "longest vertical line"
print("Tip: Look for the longest vertical distance that doesn't cross any horizontal line to find the optimal cluster count.")

# =========================================
# Training Hierarchical Clustering Model
# =========================================
# Based on the dendrogram, 5 clusters is typically optimal for this dataset
n_clusters = 5
print(f"\n--- Training Agglomerative Clustering (Clusters={n_clusters}) ---")

hc = AgglomerativeClustering(n_clusters=n_clusters, metric='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)

# Add cluster labels to the original dataframe
dataset['Cluster_Label'] = y_hc

# =========================================
# Visualizing the Clusters
# =========================================
plt.figure(figsize=(10, 7))
colors = ['red', 'blue', 'green', 'cyan', 'magenta']

for i in range(n_clusters):
    plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], 
                s=100, c=colors[i], label=f'Cluster {i+1}')

plt.title('Customer Segments (Hierarchical Clustering)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
# plt.show() # Uncomment to show the cluster scatter plot

# =========================================
# Saving Results
# =========================================
output_file = os.path.join(current_dir, "Mall_Customers_Clustered.csv")
dataset.to_csv(output_file, index=False)

print(f"\nClustering complete. Results saved to: {output_file}")
print("Workflow finished.")
