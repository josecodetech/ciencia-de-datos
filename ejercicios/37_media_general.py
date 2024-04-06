import pandas as pd

# Crear DataFrame con datos de estudiantes por promedio
estudiantes_promedio = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Laura', 'Andrés'],
    'Edad': [21, 20, 22, 19, 23],
    'Promedio': [8.5, 7.8, 9.2, 8.0, 8.9]
}
df_estudiantes_promedio = pd.DataFrame(estudiantes_promedio)

# Calcular promedio académico general de los estudiantes
promedio_general = df_estudiantes_promedio['Promedio'].mean()

print("Promedio Académico General de los Estudiantes:", promedio_general)
