import pandas as pd

# Crear un DataFrame de Pandas con datos ficticios
data = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
        'Edad': [30, 35, 40, 25],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(data)
print("DataFrame creado:\n", df)

# Filtrar los datos para mostrar solo las personas mayores de 30 años
df_filtered = df[df['Edad'] > 30]
print("Personas mayores de 30 años:\n", df_filtered)
