import pandas as pd

# Crear DataFrame con datos de estudiantes por carrera
estudiantes_carrera = {
    'Nombre': ['Jose','Juan', 'María', 'Carlos', 'Laura', 'Andrés'],
    'Edad': [21, 20, 22, 19, 23, 25],
    'Carrera': ['Empresariales','Ingeniería', 'Medicina', 'Economía',
                'Empresariales', 'Informática']
}
df_estudiantes_carrera = pd.DataFrame(estudiantes_carrera)

# Calcular cantidad de estudiantes por carrera
estudiantes_por_carrera = df_estudiantes_carrera['Carrera'].value_counts()

print("Cantidad de Estudiantes por Carrera:")
print(estudiantes_por_carrera)
