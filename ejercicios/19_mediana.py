import pandas as pd

# Crear un DataFrame de Pandas con datos ficticios
datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
        'Edad': [30, 35, 40, 25],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(datos)
print("DataFrame creado:\n", df)

# Calcular la mediana de las edades en el DataFrame
median_age = df['Edad'].median()
print("Mediana de las edades:", median_age)
