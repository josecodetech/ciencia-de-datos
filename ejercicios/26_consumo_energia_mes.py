import pandas as pd
import matplotlib.pyplot as plt
# Crear DataFrame con datos de consumo de energía por mes
consumo_energia = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Consumo': [500, 550, 600, 580, 620]
}
df_consumo_energia = pd.DataFrame(consumo_energia)

# Visualizar consumo de energía por mes
plt.figure(figsize=(8, 6))
plt.plot(df_consumo_energia['Mes'], df_consumo_energia['Consumo'], marker='o', color='red')
plt.title('Consumo de Energía por Mes')
plt.xlabel('Mes')
plt.ylabel('Consumo de Energía')
plt.grid(True)
plt.show()
