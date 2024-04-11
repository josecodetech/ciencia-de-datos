import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de empleados por edad
empleados = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Laura', 
               'Andrés'],
    'Edad': [32, 25, 25, 28, 32]
}
df_empleados = pd.DataFrame(empleados)

# Visualizar distribución de edad de los empleados
plt.figure(figsize=(8, 6))
plt.hist(df_empleados['Edad'], bins=5, color='green', 
         alpha=0.7)
plt.title('Distribución de Edad de los Empleados')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
