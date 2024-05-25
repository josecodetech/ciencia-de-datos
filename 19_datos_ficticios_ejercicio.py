import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
fake = Faker('es_ES')
# generamos datos
numero = 500
datos = {
    'Nombre':[fake.name() for _ in range(numero)],
    'Direccion':[fake.address() for _ in range(numero)],
    'Email': [fake.address() for _ in range(numero)],
    'Ventas':[fake.random_int(min=1000, max=5000) for _ in range(numero)]
}
# creamos dataframe
df = pd.DataFrame(datos)
print(df.head())
# resumen estadistico
print(df['Ventas'].describe())
# comprobamos faltantes
print(df.isnull().sum())
# grafica distribucion de ventas
plt.figure(figsize=(10,6))
plt.hist(df['Ventas'], bins=20, color='blue', edgecolor='black')
plt.title('Distribucion de ventas')
plt.xlabel('Ventas')
plt.ylabel('Cantidad')
plt.grid(True)
plt.show()
# grafica de box plot
plt.figure(figsize=(8, 6))
plt.boxplot(df['Ventas'])
plt.title('box plot de Ventas')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()
# scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(range(len(df)), df['Ventas'], color='red')
plt.title('Ventas por registro')
plt.xlabel('Indice')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()