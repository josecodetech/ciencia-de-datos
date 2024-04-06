import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# cargar datos
datos = load_iris()
X = datos.data
y = datos.target
# entrenar el modelo PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(X)
print('*'*25)
print(X_pca)
# visualiza datos
plt.scatter(X_pca[:,0],X_pca[:,1],c=y,cmap='viridis')
plt.title('PCA')
plt.xlabel('Componente principal 1')
plt.ylabel('Componente principal 2')
plt.show()