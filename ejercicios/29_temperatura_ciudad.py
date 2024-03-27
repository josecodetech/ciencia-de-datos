import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de temperaturas
temperaturas = {
    'Ciudad': ['Ciudad A', 'Ciudad B', 'Ciudad C', 'Ciudad D'],
    'Enero': [25, 28, 23, 30],
    'Febrero': [27, 29, 24, 31],
    'Marzo': [28, 30, 25, 32]
}
df_temperaturas = pd.DataFrame(temperaturas)

# Visualizar evolución de las temperaturas por ciudad
plt.figure(figsize=(10, 6))
for ciudad in df_temperaturas['Ciudad']:
    plt.plot(df_temperaturas.columns[1:], 
             df_temperaturas[df_temperaturas['Ciudad'] == ciudad].values[0][1:], 
             marker='o', label=ciudad)

plt.title('Evolución de Temperaturas por Ciudad')
plt.xlabel('Mes')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()
