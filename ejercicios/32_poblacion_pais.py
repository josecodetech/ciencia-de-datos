import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de población por país
poblacion_pais = {
    'País': ['EE. UU.', 'China', 'India', 'Brasil', 'Rusia'],
    'Población (millones)': [330, 1400, 1400, 210, 145]
}
df_poblacion_pais = pd.DataFrame(poblacion_pais)

# Visualizar población por país
plt.figure(figsize=(8, 6))
plt.bar(df_poblacion_pais['País'], 
        df_poblacion_pais['Población (millones)'], color='blue')
plt.title('Población por País')
plt.xlabel('País')
plt.ylabel('Población (millones)')
plt.grid(True)
plt.show()
