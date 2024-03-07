import numpy as np

# Crear un array de numpy con datos aleatorios
datos = np.random.randint(0, 100, size=(10,))
print("Datos generados aleatoriamente:", datos)

# Calcular el máximo y mínimo de los datos
max_val = np.max(datos)
min_val = np.min(datos)
print("Valor máximo:", max_val)
print("Valor mínimo:", min_val)
