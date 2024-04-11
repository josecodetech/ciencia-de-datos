import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de precios de productos
precios_productos = {
    'Producto': ['Producto A', 'Producto B', 'Producto C', 
                 'Producto D', 'Producto E','Producto F'],
    'Precio (€)': [55, 45, 58, 45, 55,55]
}
df_precios_productos = pd.DataFrame(precios_productos)

# Visualizar distribución de precios de productos
plt.figure(figsize=(8, 6))
plt.hist(df_precios_productos['Precio (€)'], bins=5, 
         color='blue', alpha=0.7)
plt.title('Distribución de Precios de Productos')
plt.xlabel('Precio (€)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
