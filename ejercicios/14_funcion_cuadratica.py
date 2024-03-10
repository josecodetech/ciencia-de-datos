import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo para graficar
x = np.linspace(-10, 10, 100)
y = x ** 2

# Graficar la función cuadrática
plt.plot(x, y)
plt.title('Gráfico de la función cuadrática')
plt.xlabel('x')
plt.ylabel('x^2')
plt.grid(True)
plt.show()
