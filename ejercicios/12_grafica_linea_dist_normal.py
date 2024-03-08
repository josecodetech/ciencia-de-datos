import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios distribuidos normalmente
np.random.seed(0)  # Para reproducibilidad
n_puntos = 100  # Número de puntos
media = 0  # Media de la distribución normal
desviacion_estandar = 1  # Desviación estándar de la distribución normal
datos_normal = np.random.normal(loc=media, scale=desviacion_estandar, size=n_puntos)

# Crear valores para el eje x (simplemente números enteros para cada punto)
x = np.arange(n_puntos)

# Crear la gráfica de línea
plt.plot(x, datos_normal, marker='o', linestyle='-')

# Personalizar la gráfica
plt.title('Gráfico de Línea con Datos Distribuidos Normalmente')  # Título de la gráfica
plt.xlabel('Puntos')  # Etiqueta del eje x
plt.ylabel('Datos Aleatorios')  # Etiqueta del eje y
plt.grid(True)  # Habilitar la cuadrícula en la gráfica

# Mostrar la gráfica
plt.show()