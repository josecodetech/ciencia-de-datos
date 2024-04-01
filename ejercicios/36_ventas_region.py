import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de ventas por región
ventas_region = {
    'Región': ['Norte', 'Sur', 'Este', 'Oeste'],
    'Ventas (millones)': [10, 8, 12, 9]
}
df_ventas_region = pd.DataFrame(ventas_region)

# Visualizar distribución de ventas por región
plt.figure(figsize=(8, 6))
plt.bar(df_ventas_region['Región'], 
        df_ventas_region['Ventas (millones)'], color='green')
plt.title('Ventas por Región')
plt.xlabel('Región')
plt.ylabel('Ventas (millones)')
plt.grid(True)
plt.show()
