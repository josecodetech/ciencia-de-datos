import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
propinas = sns.load_dataset('tips')

# Calcular la propina media por día de la semana
propina_media_por_dia = propinas.groupby('day')['tip'].mean().reset_index()

# Visualizar con un gráfico de barras
plt.figure(figsize=(8, 6))
sns.barplot(data=propina_media_por_dia, x='day', y='tip', palette='Set2')
plt.title('Propina Media por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Propina Media ($)')
plt.show()
