# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 07:10:34 2022

@author: Jose
"""

import moduloDatos as md
import pandas as pd
import matplotlib.pyplot as plt

# carga de datos
ruta = 'D:\\workspace\\WorkspaceTutorialCienciaDatos\\datos\\'
fichero = 'datosModificados.csv'
datos = md.cargaDatos(ruta, fichero,',')
print(datos.head())
# columna indice
datos.set_index('indice', inplace=True)
print(datos.head())
# Columnas con nulos
columnas_nulos = [ col for col in datos.columns if datos[col].isnull().any()]
print(columnas_nulos)
# Columnas
print(md.dameColumnas(datos))
# Hot encoding

datos_dummies = md.obtenerDummies(datos, 'combustible')
print(datos_dummies.head())
datos = pd.concat([datos,datos_dummies],axis=1)
print(datos.columns)

# Normalizacion
datos = md.normalizaColumna(datos, 'motor')
datos = md.normalizaColumna(datos, 'potencia')

from sklearn.linear_model import LinearRegression
# Creamos regresion lineal
lm = LinearRegression()
# Definimos variables predictoras y variable objetivo
X = datos[[ 'motor', 'potencia',
'asientos', 'CNG', 'Diesel', 'Electric',
'LPG', 'Petrol']]
print(X)

y = datos['precio']

print(X)
print('*'*100)
print(y)
print('*'*100)
# Entrenamiento o ajuste
lm.fit(X,y)
# prediccion
prediccion = lm.predict(X)
a = lm.intercept_
b = lm.coef_
# Mostramos ecuacion
#print(f'y={a}+{b1}*x1 + b2*x2 +b3*x3 ')
print('*'*100)
print('Prediccion')
print(prediccion)
print(y)
print(lm.score(X,y))

# Comparativa
resultado ={'Real':datos['precio'],'Prediccion':prediccion}
R = pd.DataFrame(data=resultado)
print(R.head())

from sklearn import metrics
ECM = metrics.mean_squared_error(datos['precio'], prediccion)
print(ECM)
r_cuadrado = metrics.r2_score(datos['precio'], prediccion)
print(r_cuadrado)

# Grafica
#plt.plot(datos['motor'],prediccion,'r',label='Prediccion')
plt.scatter(datos['motor'],y,label='Datos')
plt.scatter(datos['motor'],prediccion,c='red',label='Prediccion')
plt.title('Regresion lineal')
plt.xlabel('Motor')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()

























