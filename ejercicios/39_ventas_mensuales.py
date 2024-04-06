import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de ventas mensuales
ventas_mensuales = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas (€)': [10000, 12000, 15000, 11000, 13000]
}
df_ventas_mensuales = pd.DataFrame(ventas_mensuales)

# Visualizar evolución de las ventas mensuales
plt.figure(figsize=(8, 6))
plt.plot(df_ventas_mensuales['Mes'], 
         df_ventas_mensuales['Ventas (€)'], marker='o', color='blue')
plt.title('Evolución de las Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas (€)')
plt.grid(True)
plt.show()
