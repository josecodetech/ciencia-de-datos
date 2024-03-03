import pandas as pd
import matplotlib.pyplot as plt
# Crear un DataFrame de Pandas con datos de ejemplo
data = {'Nombre': ['Ana', 'Juan', 'María', 'Pedro'],
        'Edad': [25, 35, 35, 19],
        'Género': ['F', 'M', 'F', 'M']}
df = pd.DataFrame(data)
print("DataFrame creado:\n", df)
# Graficar un histograma de las edades
df['Edad'].plot(kind='hist', title='Histograma de Edades') 
plt.show()