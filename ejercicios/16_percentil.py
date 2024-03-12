import numpy as np

# Crear un array de numpy con datos aleatorios
datos = np.random.normal(loc=50, scale=20, size=(100,))

# Calcular el percentil 25 y 75 de los datos
percentil_25 = np.percentile(datos, 25)
percentil_75 = np.percentile(datos, 75)
print("Percentil 25:", percentil_25)
print("Percentil 75:", percentil_75)
