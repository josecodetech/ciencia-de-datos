import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_samples, silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# generamos datos 
X, _ = make_blobs(n_samples=250, centers = 4, cluster_std=0.60, random_state=0)
# print(X)
# calcular dendrograma
Z = linkage(X, 'ward')
# visualiza el dendrograma
plt.figure(figsize=(10,5))
plt.title('Dendrograma')
plt.xlabel('Indice de muestra')
plt.ylabel('Distancia')
dendrogram(Z, leaf_rotation=90, leaf_font_size=6)
plt.show()
# entrenar modelo de clustering jerarquico
hierarchical = AgglomerativeClustering(n_clusters=4)
labels = hierarchical.fit_predict(X)
# calcular indice de silueta
silhouette_avg = silhouette_score(X, labels)
print(f"Indice de silueta promedio: {silhouette_avg:.2f}")
# calcular valores de silueta para cada muestra
sample_silhouette_values = silhouette_samples(X, labels)
# visualizar grafica de silueta
plt.figure(figsize=(10, 5))
y_lower = 10
for i in range(4):
    ith_cluster_silhouette_values = sample_silhouette_values[labels == i]
    ith_cluster_silhouette_values.sort()
    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i
    color = plt.cm.nipy_spectral(float(i) / 4)
    plt.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)
    plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
    y_lower = y_upper + 10
plt.title('Grafica de silueta')
plt.xlabel('Coeficiente de silueta')
plt.ylabel('Clusters')
plt.axvline(x=silhouette_avg, color='red', linestyle='--')
plt.yticks([])
plt.show()