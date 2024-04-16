import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de compras en línea
compras_en_linea = {
    'Día de la Semana': ['Lunes', 'Martes', 'Miércoles', 
                         'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    'Compras': [100, 120, 130, 140, 130, 160, 70]
}
df_compras_en_linea = pd.DataFrame(compras_en_linea)

# Visualizar distribución de compras por día de la semana
plt.figure(figsize=(8, 6))
plt.bar(df_compras_en_linea['Día de la Semana'], 
        df_compras_en_linea['Compras'], color='red')
plt.title('Compras en Línea por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Compras')
plt.grid(True)
plt.show()
