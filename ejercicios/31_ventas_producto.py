import pandas as pd

# Crear DataFrame con datos de ventas por producto
ventas_productos = {
    'Producto': ['Producto A', 'Producto B', 
                 'Producto C', 'Producto D',
                 'Producto C', 'Producto D'],
    'Ventas': [100, 150, 120, 200, 500, 400]
}
df_ventas_productos = pd.DataFrame(ventas_productos)

# Calcular cantidad total de ventas por producto
total_ventas_por_producto = df_ventas_productos.groupby('Producto')['Ventas'].sum()

print("Total de Ventas por Producto:")
print(total_ventas_por_producto)
