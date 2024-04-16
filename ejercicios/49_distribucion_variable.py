import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
propinas = sns.load_dataset('tips')

# Visualizar la distribución de la variable "total_bill"
plt.figure(figsize=(10, 6))
sns.histplot(propinas['total_bill'], kde=True, color='skyblue')
plt.title('Distribución del Total de la Cuenta')
plt.xlabel('Total de la Cuenta ($)')
plt.ylabel('Frecuencia')
plt.show()
