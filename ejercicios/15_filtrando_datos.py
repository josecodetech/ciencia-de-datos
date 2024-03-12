import pandas as pd

# Crear un DataFrame de Pandas con datos de ejemplo
datos = {'Nombre': ['Ana', 'Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 35, 40],
        'Género': ['F', 'M', 'F', 'M']}
df = pd.DataFrame(datos)
print("DataFrame creado:\n", df)

# Filtrar los datos para mostrar solo las personas de género femenino
df_filtrado = df[df['Género'] == 'F']
print("Personas de género femenino:\n", df_filtrado)
