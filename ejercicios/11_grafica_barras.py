import pandas as pd
import matplotlib.pyplot as plt


# Crear un DataFrame de Pandas con datos de ejemplo
data = {'Nombre': ['Ana', 'Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 35, 30],
        'Género': ['F', 'M', 'F', 'M']}
df = pd.DataFrame(data)
print("DataFrame creado:\n", df)

# Graficar un diagrama de barras de las edades
df['Edad'].plot(kind='bar', 
                title='Diagrama de Barras de Edades')
plt.show()
