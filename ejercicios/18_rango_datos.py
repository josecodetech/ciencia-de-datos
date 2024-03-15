import numpy as np

# Crear un array de numpy con datos aleatorios
datos = np.random.randint(0, 100, size=(10,))
print("Datos generados aleatoriamente:", datos)

# Calcular el rango de los datos
rango = np.max(datos) - np.min(datos)
print("Rango de los datos:", rango)
