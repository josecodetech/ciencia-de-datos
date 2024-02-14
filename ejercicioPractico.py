import pandas as pd
df_ventas = pd.read_csv('ventas.csv',sep=';')
print(df_ventas.head())
df_ventas.fillna(0,inplace=True)
df_ventas['Ingresos'] = df_ventas['Cantidad'] * df_ventas['Precio_Unitario']
print(df_ventas.head())
ingresos_por_tienda_producto = df_ventas.groupby(['Tienda','Producto'])['Ingresos'].sum().reset_index()
print(ingresos_por_tienda_producto)
producto_top_por_tienda = ingresos_por_tienda_producto.sort_values(['Tienda','Ingresos'],ascending=[True, False]).groupby('Tienda').first().reset_index()
print(producto_top_por_tienda)
resumen_cantidad = df_ventas.groupby('Producto')['Cantidad'].sum().reset_index()
print('Resumen: ')
print(resumen_cantidad)
resumen_cantidad.to_csv('resumen_ventas.csv',index=False)