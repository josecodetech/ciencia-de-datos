import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.normal(0,0.5,100)
y = np.random.normal(0,0.5,100) 
x[98:] =[3,-3]
y[98:] =[3,-3]
print(x)
print(y)
plt.scatter(x,y)
plt.title("Scatter Plot con Outliers")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
distancia_centro = np.sqrt(x**2+y**2)
limite = np.percentile(distancia_centro,95) #umbral del 95%
x_filtrado = x[distancia_centro <= limite]
y_filtrado = y[distancia_centro <= limite]
print('-'*35)
print(distancia_centro)
print(limite)
print(x_filtrado)
print(y_filtrado)
plt.scatter(x_filtrado,y_filtrado)
plt.title("Scatter Plot sin Outliers")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()