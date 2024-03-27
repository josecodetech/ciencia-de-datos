import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de redes sociales
redes_sociales = {
    'Plataforma': ['Facebook', 'Instagram', 'Twitter', 
                   'LinkedIn'],
    'Usuarios': [500, 800, 300, 200]
}
df_redes_sociales = pd.DataFrame(redes_sociales)

# Visualizar frecuencia de uso de redes sociales
plt.figure(figsize=(8, 6))
plt.bar(df_redes_sociales['Plataforma'], 
        df_redes_sociales['Usuarios'], color='orange')
plt.title('Frecuencia de Uso de Redes Sociales')
plt.xlabel('Plataforma')
plt.ylabel('Usuarios')
plt.grid(True)
plt.show()
