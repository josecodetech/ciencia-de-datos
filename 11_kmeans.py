import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
# carga de datos
datos = load_iris()
X = pd.DataFrame(datos.data, columns=datos.feature_names)
print(X.info())
print('*'*25)
print(X.describe())
print('*'*25)
print(X.head())
print('*'*25)
# escalar los datos
scaler = StandardScaler()
X_escalado = scaler.fit_transform(X)
# crear y entrenar el modelo
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_escalado)
# obtener etiquetas de cluster y asignarla a los datos
etiquetas = kmeans.labels_
X['cluster'] = etiquetas
print(X.tail(25))
# visualizacion
plt.scatter(X['sepal length (cm)'], X['sepal width (cm)'], c=X['cluster'],cmap='viridis')
plt.xlabel('Longitud sepalo')
plt.ylabel('Ancho sepalo')
plt.title("Clasificacion por clusters con K-Means")
plt.show()
