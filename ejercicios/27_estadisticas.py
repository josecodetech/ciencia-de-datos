import pandas as pd
import numpy as np

# Crear DataFrame con datos de estudiantes
estudiantes = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Laura', 
               'Andrés'],
    'Edad': [21, 20, 22, 19, 23],
    'Género': ['Masculino', 'Femenino', 'Masculino', 
               'Femenino', 'Masculino']
}
df_estudiantes = pd.DataFrame(estudiantes)

# Calcular estadísticas básicas por género
estadisticas_por_genero = df_estudiantes.groupby('Género').agg({'Edad': 
    ['mean', 'median', 'min', 'max']})

print("Estadísticas por Género:")
print(estadisticas_por_genero)
