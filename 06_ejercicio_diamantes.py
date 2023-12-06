import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

datos = sns.load_dataset('diamonds')
df = pd.DataFrame(datos)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
# df_limpio = df.dropna()
# grafica
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['carat'],kde=True)
plt.title('Distribucion de peso en quilates')
plt.xlabel('Peso en quilates')
plt.ylabel('Frecuencia')
plt.subplot(1, 2, 2)
sns.histplot(df['price'],kde=True)
plt.xlabel('Precio en dolares')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()
# relacion peso precio
plt.figure(figsize=(10, 5))
sns.scatterplot(x='carat', y='price', data=df, alpha=0.5)
plt.title('Relacion peso precio')
plt.xlabel('Peso en quilates')
plt.ylabel('Precio en dolares')
plt.show()
# boxplot precio por claridad
plt.figure(figsize=(8, 5))
sns.boxplot(x='clarity', y='price', data=df, order= ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
plt.title('Precio por claridad')
plt.xlabel('Claridad')
plt.ylabel('Precio en dolares')
plt.show()
