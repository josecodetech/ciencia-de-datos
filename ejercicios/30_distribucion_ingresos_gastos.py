import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de ingresos y gastos
ingresos_gastos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ingresos': [5000, 5500, 6000, 5800],
    'Gastos': [4000, 4500, 4800, 5000]
}
df_ingresos_gastos = pd.DataFrame(ingresos_gastos)

# Visualizar distribución de ingresos y gastos mensuales
plt.figure(figsize=(10, 6))
plt.plot(df_ingresos_gastos['Mes'], df_ingresos_gastos['Ingresos'], 
         marker='o', color='green', label='Ingresos')
plt.plot(df_ingresos_gastos['Mes'], df_ingresos_gastos['Gastos'], 
         marker='o', color='red', label='Gastos')
plt.title('Distribución de Ingresos y Gastos Mensuales')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.legend()
plt.grid(True)
plt.show()
