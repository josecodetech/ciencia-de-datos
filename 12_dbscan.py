import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
# datos
X, _ = make_moons(n_samples=1000, noise=0.05)
# print(X)
# entrenar el modelo
dbscan = DBSCAN(eps=0.2, min_samples=5)
dbscan.fit(X)
# visualizar los resultados del clustering
labels = dbscan.labels_
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title('DBSCAN Clustering')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')
plt.show()