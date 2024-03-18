import pandas as pd
import matplotlib.pyplot as plt
# Crear DataFrame con datos de ventas por producto
ventas_producto = {
    'Producto': ['Producto A', 'Producto B', 
                 'Producto C', 'Producto D'],
    'Ventas': [200, 300, 250, 400]
}
df_ventas_producto = pd.DataFrame(ventas_producto)

# Visualizar ventas por producto
plt.figure(figsize=(8, 6))
plt.bar(df_ventas_producto['Producto'], 
        df_ventas_producto['Ventas'], color='purple')
plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()
