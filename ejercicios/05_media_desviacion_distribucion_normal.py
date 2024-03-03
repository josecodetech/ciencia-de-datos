import numpy as np

# Crear un array de numpy con datos aleatorios
data = np.random.normal(loc=0, scale=1, size=(100,))

# Calcular la media y la desviación estándar de los datos
mean = np.mean(data)
std_dev = np.std(data)
print("Media:", mean)
print("Desviación estándar:", std_dev)
