import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de ingresos por sector
ingresos_sector = {
    'Sector': ['Tecnología', 'Finanzas', 'Salud', 
               'Educación'],
    'Ingresos (millones $)': [500, 300, 400, 250]
}
df_ingresos_sector = pd.DataFrame(ingresos_sector)

# Visualizar distribución de ingresos por sector
plt.figure(figsize=(8, 6))
plt.bar(df_ingresos_sector['Sector'], 
        df_ingresos_sector['Ingresos (millones $)'], 
        color='purple')
plt.title('Ingresos por Sector')
plt.xlabel('Sector')
plt.ylabel('Ingresos (millones $)')
plt.grid(True)
plt.show()



