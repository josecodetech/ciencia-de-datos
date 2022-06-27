# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 07:44:26 2022

@author: Jose
"""

import moduloDatos as md
import matplotlib.pyplot as plt

# carga de datos
ruta = 'D:\\workspace\\WorkspaceTutorialCienciaDatos\\datos\\'
fichero = 'precios_coches02.csv'
datos = md.cargaDatos(ruta, fichero,';')
print(datos.head())
# columna indice
datos.set_index('Unnamed: 0', inplace=True)
datos.index.name = 'indice'
print(datos.head())
# cambio nombre columnas
print(md.dameColumnas(datos))
nombre_columnas = ['nombre','localizacion','año','kilometros recorridos','combustible','transmision','tipo propietario', 'kilometraje','motor','potencia','asientos','nuevo precio','precio']
md.cambiaColumnas(datos, nombre_columnas)
print(md.dameColumnas(datos))
# estadisticos basicos
print(md.dameEstadisticos(datos))
print('*'*100)
print('*'*100)
print(md.dameEstadisticos(datos,'all'))
# valores nulos
datos = md.reemplazarNulos(datos, 'asientos')
print(md.dameEstadisticos(datos))
# cambio tipo
print(datos['motor'])
print(datos['potencia'])
datos['potencia']=md.cambiaTipo(datos['potencia'])
datos = md.reemplazarNulos(datos, 'potencia')
print(datos['potencia'])
print(datos.info)
print(datos['nombre'].value_counts())

# visualizacion datos
plt.boxplot(datos['precio'])
plt.title('Precios')
plt.show()

# grafico de dispersion relacion entre variables
y = datos['precio']
x = datos['potencia']
plt.scatter(x,y)
plt.title('Potencia / Precio')
plt.xlabel('Potencia')
plt.ylabel('Precio')
plt.show()

x = datos['motor']
plt.scatter(x,y)
plt.title('Motor / Precio')
plt.xlabel('Motor')
plt.ylabel('Precio')
plt.show()

# mediante coeficiente de correlacion y p valor
# si prox a 1 relacion positiva
# si prox a -1 relacion negativa
# si prox a 0 sin relacion
# p valor
# si <0.001 fuerte certeza en el resultado
# si <0.05 moderado
# si <0.1 baja o debil
# si >0.1 sin certeza de correlacion

from scipy import stats
datos = md.reemplazarNulos(datos, 'motor')
datos = md.reemplazarNulos(datos, 'precio')
pearson_coef, p_valor = stats.pearsonr(datos['motor'],datos['precio'])
print(f"El coeficiente de correlacion de Pearson es : {pearson_coef}")
print(f"El p-valor es : {p_valor}")

columnas = ['nombre','año','kilometros recorridos','motor','potencia','precio']

datos_nuevos = datos[columnas]
print(datos_nuevos.head())
datos_agrupados = datos_nuevos.groupby(['año'],as_index=False).mean()
print(datos_agrupados.head())

# guardamos datos
fichero='datosModificados.csv'
md.guardarDatos(datos, ruta, fichero)



















