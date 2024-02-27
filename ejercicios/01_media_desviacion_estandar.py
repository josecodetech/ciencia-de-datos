import numpy as np

# Crear un array de numpy con datos aleatorios
data = np.random.normal(loc=50, scale=10, size=(100,))
print("Datos generados aleatoriamente:", data)

# Calcular la media y la desviación estándar de los datos
mean = np.mean(data)
std_dev = np.std(data)
print("Media:", mean)
print("Desviación estándar:", std_dev)
