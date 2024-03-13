import pandas as pd

# Crear un DataFrame de Pandas con datos ficticios
datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
        'Edad': [30, 35, 40, 25],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(datos)
print("DataFrame creado:\n", df)

# Calcular la edad promedio de las personas en el DataFrame
promedio_edad = df['Edad'].mean()
print("Edad promedio:", promedio_edad)
