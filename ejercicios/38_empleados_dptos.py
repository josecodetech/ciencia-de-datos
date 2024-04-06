import pandas as pd

# Crear DataFrame con datos de empleados por departamento
empleados_departamento = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Laura', 'Andrés','Jose'],
    'Edad': [30, 25, 35, 28, 32, 42],
    'Departamento': ['Ventas', 'Contabilidad', 'Producción', 
                     'Recursos Humanos', 'Tecnología','Contabilidad']
}
df_empleados_departamento = pd.DataFrame(empleados_departamento)

# Calcular cantidad de empleados por departamento
empleados_por_departamento = df_empleados_departamento['Departamento'].value_counts()

print("Cantidad de Empleados por Departamento:")
print(empleados_por_departamento)
