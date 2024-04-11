import pandas as pd

# Crear DataFrame con datos de calificaciones de estudiantes
calificaciones_estudiantes = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Laura', 'Andrés'],
    'Matemáticas': [4, 7, 9, 8, 7],
    'Ciencias': [7, 8, 8, 9, 7],
    'Historia': [9, 8, 5, 8, 9]
}
df_calificaciones_estudiantes = pd.DataFrame(calificaciones_estudiantes)

# Calcular promedio académico de los estudiantes
df_calificaciones_estudiantes['Promedio'] = round(df_calificaciones_estudiantes.mean(axis=1),2)

print("Calificaciones de Estudiantes:")
print(df_calificaciones_estudiantes)
