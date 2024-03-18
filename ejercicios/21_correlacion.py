import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de rendimiento académico
datos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [18, 17, 19, 18],
    'Nota_Matematicas': [85, 90, 75, 80],
    'Nota_Lenguaje': [70, 80, 85, 75]
}
df = pd.DataFrame(datos)
# Calcular matriz de correlación
correlacion = df[['Nota_Matematicas', 'Nota_Lenguaje']].corr()

# Visualizar matriz de correlación como un mapa de calor
plt.figure(figsize=(8, 6))
plt.imshow(correlacion, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlacion)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion)), correlacion.columns)
plt.title('Matriz de Correlación')
plt.show()
