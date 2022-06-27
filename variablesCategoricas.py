# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 07:36:31 2022

@author: Jose
"""

import pandas as pd


fichero = 'D:\workspace\WorkspaceTutorialCienciaDatos\datos\precios_coches.csv'


datos = pd.read_csv(fichero)
print(datos.columns)
print(datos['Fuel_Type'])

# transformar variable categorica en dummies (ficticia)
columna_dummies = pd.get_dummies(datos['Fuel_Type'])
print(columna_dummies)

datos_dummies = pd.get_dummies(datos,columns=['Fuel_Type'])
print(datos.head)
print("*"*25)
print("*"*25)
print(datos_dummies.head())