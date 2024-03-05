import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo para graficar
x = np.linspace(0, 10, 100)
y = np.cos(x)

# Graficar la función coseno
plt.plot(x, y)
plt.title('Gráfico de la función coseno')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid(True)
plt.show()
