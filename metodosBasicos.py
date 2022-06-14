# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:42:37 2022

@author: Jose
"""

import pandas as pd
import numpy as np

#pip install pandas

fichero = 'D:\workspace\WorkspaceTutorialCienciaDatos\datos\precios_coches.csv'

#datos = pd.read_csv(fichero, header=None)
datos = pd.read_csv(fichero)

print(datos.dtypes)

print(datos.describe())

print(datos.describe(include='all'))

print(datos.info())

# preprocesamiento datos
print(datos['Seats'].head(5))
#datos['Seats'] = datos['Seats'] -1
print(datos['Seats'])

print(datos.describe())

# Sustitucion valores faltantes
#datos.dropna(subset=['Seats'],axis=0,inplace=True)
#-datos.replace(np.nan,'nulo')
media_asientos = datos['Seats'].mean()
print(media_asientos)
datos['Seats'].replace(np.nan,media_asientos,inplace=True)
print(datos.describe())

#print(datos['Seats']>5)


