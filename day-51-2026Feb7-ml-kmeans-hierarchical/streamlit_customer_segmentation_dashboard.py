"""
File Name   : streamlit_customer_segmentation_dashboard.py
Purpose     : Streamlit app for Customer Segmentation (K-Means & Hierarchical)
Dataset     : Mall_Customers.csv
Author      : Venkatesh Singamsetty
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.cluster.hierarchy as sch
from sklearn.cluster import KMeans, AgglomerativeClustering

# Title
st.title("Customer Segmentation Dashboard")

# Load dataset using relative path
current_dir = os.path.dirname(__file__)
dataset_path = os.path.join(current_dir, "Mall_Customers.csv")

# Guard clause for dataset existence
if not os.path.exists(dataset_path):
    st.error(f"Dataset not found at: {dataset_path}")
    st.stop()

# --- Load Data ---
dataset = pd.read_csv(dataset_path)
X = dataset.iloc[:, [3, 4]].values

# --- Sidebar Configuration ---
st.sidebar.header("Settings")
algo = st.sidebar.selectbox("Select Clustering Algorithm", ("K-Means", "Hierarchical"))
n_clusters = st.sidebar.slider("Number of clusters", 2, 10, 5)

# --- Model Execution ---
if algo == "K-Means":
    st.subheader("K-Means Clustering Analysis")
    model = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    y_pred = model.fit_predict(X)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', s=100)
    ax.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=300, c='red', marker='X', label='Centroids')
    ax.set_title(f'K-Means Clusters (k={n_clusters})')

else:
    st.subheader("Hierarchical Clustering Analysis")
    
    # Option to show Dendrogram
    if st.checkbox("Show Dendrogram"):
        st.write("Generating Dendrogram to identify optimal clusters...")
        fig_den, ax_den = plt.subplots(figsize=(10, 6))
        dendrogram = sch.dendrogram(sch.linkage(X, method='ward'), ax=ax_den)
        ax_den.set_title('Dendrogram')
        ax_den.set_xlabel('Customers')
        ax_den.set_ylabel('Euclidean distances')
        st.pyplot(fig_den)

    model = AgglomerativeClustering(n_clusters=n_clusters, metric='euclidean', linkage='ward')
    y_pred = model.fit_predict(X)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='rainbow', s=100)
    ax.set_title(f'Hierarchical Clusters (n={n_clusters})')

# Common axis labels
ax.set_xlabel('Annual Income (k$)')
ax.set_ylabel('Spending Score (1-100)')
ax.legend()
st.pyplot(fig)

# --- Data Table ---
st.subheader("Clustered Data Results")
dataset['cluster'] = y_pred
st.dataframe(dataset)
