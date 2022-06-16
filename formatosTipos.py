# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:42:37 2022

@author: Jose
"""

import pandas as pd
import numpy as np

#pip install pandas

fichero = 'D:\workspace\WorkspaceTutorialCienciaDatos\datos\precios_coches.csv'

datos = pd.read_csv(fichero)
print(datos.head())

print(datos.dtypes)
# cambiamos tipo de datos
datos['Unnamed: 0']=datos['Unnamed: 0'].astype('float64')
print(datos.dtypes)
# realizar calculos y ponerlos en otra columna

# millas = kilometros * 0,621371
datos['millas_driven']=datos['Kilometers_Driven']*0.621371
print(datos.head())

# renombrar columna
datos.rename(columns={'millas_driven':'Millas'},inplace=True)
print(datos.head())

# noramilizar datos
# min y valor anterior
print(datos[['Millas','Kilometers_Driven']])
datos['Millas_normalizadas']=datos['Millas']/datos['Millas'].max()
datos['Kilometros_normalizados']=datos['Kilometers_Driven']/datos['Kilometers_Driven'].max()
print(datos[['Millas_normalizadas','Kilometros_normalizados']])
# min max
print(datos[['Millas','Kilometers_Driven']])
datos['Millas_normalizadas']=(datos['Millas']-datos['Millas'].min())/(datos['Millas'].max()-datos['Millas'].min())
datos['Kilometros_normalizados']=(datos['Kilometers_Driven']-datos['Kilometers_Driven'].min())/(datos['Kilometers_Driven'].max()-datos['Kilometers_Driven'].min())
print(datos[['Millas_normalizadas','Kilometros_normalizados']])


















