import pandas as pd

# Crear un DataFrame de Pandas con datos ficticios
data = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
        'Edad': [30, 35, 40, 25],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(data)
print("DataFrame creado:\n", df)

# Filtrar los datos para mostrar solo las personas que viven en Madrid
df_filtrado = df[df['Ciudad'] == 'Madrid']
print("Personas que viven en Madrid:\n", df_filtrado)
