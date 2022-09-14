import streamlit as st
import pandas as pd
file = "C:\Users\acer\Your team Dropbox\MUHAMMAD ZULHILMI DAUD\PC\Desktop\AIRASIA ACADEMY - DATA ANALYST\Python\datasets-20220911T063729Z-001\datasets"
df = pd.read_csv(file)
from sklearn.cluster import KMeans

st.write("""
# Kmeans Clustering for Mall Customer
This app is to show the relation between **Income** and **Spending**.
""")
mallcust = datasets.load_mall_customer()
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.scatter(X['Annual_Income_(k$)'], X['Spending_Score'], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='black', s=200, alpha=0.5);
