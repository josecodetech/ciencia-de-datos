import pandas as pd
import matplotlib.pyplot as plt
# Crear un DataFrame de Pandas con datos de ejemplo
data = {'Nombre': ['Ana', 'Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27, 40],
        'Género': ['F', 'M', 'F', 'M']}
df = pd.DataFrame(data)
print("DataFrame creado:\n", df)
# Graficar un diagrama de dispersión de las edades
df.plot(kind='scatter', x='Nombre', y='Edad', 
        title='Diagrama de Dispersión de Edades')
plt.show()