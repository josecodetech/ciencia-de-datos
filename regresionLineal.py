# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 07:38:33 2022

@author: Jose
"""

import moduloDatos as md

# carga de datos
ruta = 'D:\\workspace\\WorkspaceTutorialCienciaDatos\\datos\\'
fichero = 'datosModificados.csv'
datos = md.cargaDatos(ruta, fichero,',')
print(datos.head())
# columna indice
datos.set_index('indice', inplace=True)
print(datos.head())

from sklearn.linear_model import LinearRegression
# Creamos regresion lineal
lm = LinearRegression()
# Definimos variables predictoras y variable objetivo
X = datos[['motor']]
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
print(f'y={a}+{b}*x')
print('*'*100)
print('Prediccion')
print(prediccion)
print(y)
print(lm.score(X,y))
# Visualizacion
import seaborn as sns
sns.regplot(x='motor',y='precio',data=datos)

# visualizar residuales, prediccion - error
sns.residplot(datos['motor'],datos['precio'])


# Separando en entrenamiento y pruebas

# Definimos variables predictoras y variable objetivo
X = datos[['motor']]
y = datos['precio']
# Separamos en entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

print(X_train)
print('*'*100)
print(y_train)
print('*'*100)
# Entrenamiento o ajuste
lm.fit(X_train,y_train)
# prediccion
prediccion = lm.predict(X_test)
a = lm.intercept_
b = lm.coef_
# Mostramos ecuacion
print(f'y={a}+{b}*x')
print('*'*100)
print('Prediccion')
print(prediccion)
print(y_test)
print(lm.score(X_train,y_train))
# Visualizacion
import seaborn as sns
sns.regplot(x='motor',y='precio',data=datos)

# visualizar residuales, prediccion - error
sns.residplot(datos['motor'],datos['precio'])











