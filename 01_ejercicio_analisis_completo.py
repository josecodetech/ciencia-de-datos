import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = {
    'Fecha':pd.date_range(start='2023-01-01',end='2023-01-10'),
    'Producto':['A','B','A','C','B','C','A','B','C','A'],
    'Ventas':[100,46,87,86,98,79,110,211,312,415]
}
df = pd.DataFrame(datos)
# guardamos datos en archivo
df.to_csv('ventas.csv',index=False)
# cargamos datos
df = pd.read_csv('ventas.csv')
# mostrar primeras filas
print(df.head())
# informacion general del dataframe
print(df.info())
# estadisticas descriptivas
print(df.describe())
# numero de valores unicos
print(df['Producto'].value_counts())
# visualizacion, graficas
# grafica de barras
plt.bar(df['Producto'],df['Ventas'])
plt.title('Ventas por producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.show()
# grafica de lineas, tendencia de ventas por tiempo
plt.plot(df['Fecha'],df['Ventas'],marker='o')
plt.title('Tendencia de ventas a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.show()