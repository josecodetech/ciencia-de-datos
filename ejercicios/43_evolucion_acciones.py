import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de acciones
acciones = {
    'Fecha': ['2022-01-01', '2022-02-01', '2022-03-01', 
              '2022-04-01', '2022-05-01'],
    'AAPL': [150, 160, 155, 165, 170],
    'GOOG': [2500, 2600, 2550, 2700, 2800],
    'AMZN': [3200, 3300, 3250, 3350, 3400]
}
df_acciones = pd.DataFrame(acciones)

# Convertir la columna 'Fecha' a tipo datetime
df_acciones['Fecha'] = pd.to_datetime(df_acciones['Fecha'])

# Visualizar evolución del precio de las acciones
plt.figure(figsize=(10, 6))
plt.plot(df_acciones['Fecha'], df_acciones['AAPL'], 
         marker='o', label='AAPL')
plt.plot(df_acciones['Fecha'], df_acciones['GOOG'], 
         marker='o', label='GOOG')
plt.plot(df_acciones['Fecha'], df_acciones['AMZN'], 
         marker='o', label='AMZN')
plt.title('Evolución del Precio de las Acciones')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.legend()
plt.grid(True)
plt.show()
