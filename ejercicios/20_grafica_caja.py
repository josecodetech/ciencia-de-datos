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

# Visualizar distribución de notas
plt.figure(figsize=(10, 6))
df[['Nota_Matematicas', 'Nota_Lenguaje']].boxplot()
plt.title('Distribución de Notas')
plt.ylabel('Nota')
plt.show()
