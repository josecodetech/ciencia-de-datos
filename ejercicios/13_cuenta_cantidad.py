import pandas as pd

# Crear un DataFrame de Pandas con datos ficticios
datos = {'Nombre': ['Lucia','Juan', 'María', 'Pedro', 'Ana','Jose'],
        'Edad': [24, 30, 35, 40, 25, 52],
        'Ciudad': ['Cordoba','Madrid', 'Barcelona', 'Valencia', 'Sevilla','Sevilla']}
df = pd.DataFrame(datos)
print("DataFrame creado:\n", df)

# Calcular la cantidad de personas por ciudad
cuenta = df['Ciudad'].value_counts()
print("Cantidad de personas por ciudad:\n\n", cuenta)
