import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips_datos = sns.load_dataset('tips')
df = pd.DataFrame(tips_datos)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
# grafica total
df['total_bill'].hist()
plt.title('Distribucion del total de la cuenta')
plt.xlabel("Total de la cuenta")
plt.ylabel("Frecuencia")
plt.show()
# grafica propina
df['tip'].hist()
plt.title('Distribucion de las propinas')
plt.xlabel("Propina")
plt.ylabel("Frecuencia")
plt.show()
# grafica dispersion
plt.scatter(df['total_bill'],df['tip'])
plt.title('Relacion entre Total y Propina')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.show()
# grafica barras
df['sex'].value_counts().plot(kind='bar')
plt.title('Cantidad de Clientes por sexo')
plt.xlabel('Sexo')
plt.ylabel('Cantidad')
plt.show()


