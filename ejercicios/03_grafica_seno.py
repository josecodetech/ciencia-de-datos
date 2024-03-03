import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo para graficar
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Graficar la función seno
plt.plot(x, y)
plt.title('Gráfico de la función seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
