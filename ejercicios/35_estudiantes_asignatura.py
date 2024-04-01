import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de estudiantes por asignatura
estudiantes_asignatura = {
    'Asignatura': ['Matemáticas', 'Lenguaje', 'Ciencias', 
                   'Historia'],
    'Estudiantes': [100, 120, 90, 80]
}
df_estudiantes_asignatura = pd.DataFrame(estudiantes_asignatura)

# Visualizar estudiantes por asignatura
plt.figure(figsize=(8, 6))
plt.bar(df_estudiantes_asignatura['Asignatura'], 
        df_estudiantes_asignatura['Estudiantes'], color='green')
plt.title('Estudiantes por Asignatura')
plt.xlabel('Asignatura')
plt.ylabel('Estudiantes')
plt.grid(True)
plt.show()
