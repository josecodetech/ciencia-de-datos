import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de tiempos de entrega
tiempos_entrega = {
    'Pedido': ['Pedido A', 'Pedido B', 'Pedido C', 'Pedido D', 
               'Pedido E','Pedido F'],
    'Tiempo de Entrega (días)': [3, 1, 2, 5, 3,2]
}
df_tiempos_entrega = pd.DataFrame(tiempos_entrega)

# Visualizar distribución de tiempos de entrega
plt.figure(figsize=(8, 6))
plt.hist(df_tiempos_entrega['Tiempo de Entrega (días)'], 
         bins=5, color='orange', alpha=0.7)
plt.title('Distribución de Tiempos de Entrega')
plt.xlabel('Tiempo de Entrega (días)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
