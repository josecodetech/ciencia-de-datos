import matplotlib.pyplot as plt
import pandas as pd
# Crear DataFrame con datos de gastos mensuales
gastos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 
            'Abril', 'Mayo'],
    'Gastos': [2000, 2500, 2200, 
               2800, 3000]
}
df_gastos = pd.DataFrame(gastos)

# Visualizar gastos mensuales
plt.figure(figsize=(8, 6))
plt.plot(df_gastos['Mes'], df_gastos['Gastos'], 
         marker='o', color='blue')
plt.title('Gastos Mensuales')
plt.xlabel('Mes')
plt.ylabel('Gastos')
plt.grid(True)
plt.show()
