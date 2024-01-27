import numpy as np
import matplotlib.pyplot as plt
datos = np.array([10,12,12,13,12,11,14,13,15,64,12,14,15,12,78,13,59])
plt.boxplot(datos, vert=True)
plt.title("Boxplot de Datos con outliers")
plt.xlabel("Valores")
plt.show()
Q1 = np.percentile(datos, 25)
Q3 = np.percentile(datos, 75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
datos_filtrados = datos[(datos >= limite_inferior) & (datos <= limite_superior)]

print("Datos filtrados:", datos_filtrados)
print(limite_superior)
print(limite_inferior)
plt.boxplot(datos_filtrados, vert=True)
plt.title("Boxplot de Datos sin outliers")
plt.xlabel("Valores")
plt.show()