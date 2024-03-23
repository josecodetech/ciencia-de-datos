import pandas as pd
import matplotlib.pyplot as plt


# Crear DataFrame con datos de empleados por departamento
empleados_departamento = {
    'Departamento': ['Ventas', 'Marketing', 'Finanzas', 
                     'Producción'],
    'Empleados': [50, 30, 20, 40]
}
df_empleados_departamento = pd.DataFrame(empleados_departamento)

# Visualizar cantidad de empleados por departamento
plt.figure(figsize=(8, 6))
plt.bar(df_empleados_departamento['Departamento'],
        df_empleados_departamento['Empleados'], color='orange')
plt.title('Cantidad de Empleados por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Cantidad de Empleados')
plt.grid(True)
plt.show()
