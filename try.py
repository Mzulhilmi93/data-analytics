import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
file = "mall_customer.csv"
df = pd.read_csv(file)

st.write("""
# Kmeans Clustering for Mall Customer
This app is to show the relation between **Income** and **Spending**.
""")

features = ['Annual_Income_(k$)', 'Spending_Score']
X = df[features]
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.scatter(X['Annual_Income_(k$)'], X['Spending_Score'], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='black', s=200, alpha=0.5);
