import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.title("Customer Segmentation using K-Means")

# Load dataset
dataset = pd.read_csv("Mall_Customers.csv")
X = dataset.iloc[:, [3, 4]].values

# Sidebar for parameters
st.sidebar.header("Parameters")
n_clusters = st.sidebar.slider("Number of clusters", 1, 10, 5)

# Train K-Means model
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
y_means = kmeans.fit_predict(X)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(X[:, 0], X[:, 1], c=y_means, cmap='viridis', s=100)
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X', label='Centroids')
ax.set_title('Clusters of Customers')
ax.set_xlabel('Annual Income (k$)')
ax.set_ylabel('Spending Score (1-100)')
ax.legend()

st.pyplot(fig)

# Display dataset with cluster labels
st.subheader("Dataset with Cluster Labels")
dataset['cluster'] = y_means
st.dataframe(dataset)