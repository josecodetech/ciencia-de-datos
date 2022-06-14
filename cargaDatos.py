# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:42:37 2022

@author: Jose
"""

import pandas as pd

fichero = 'D:\workspace\WorkspaceTutorialCienciaDatos\datos\precios_coches.csv'

#datos = pd.read_csv(fichero, header=None)
datos = pd.read_csv(fichero)
#print(datos)
print(datos.head(5))
print("*"*10)
print(datos.tail(6))

print(datos.columns)

titulos_cabecera = ['indice','nombre','localizacion','año','kilometros recorridos','combustible','transmision','tipo propietario', 'kilometraje','motor','potencia','asientos','precio']

datos.columns = titulos_cabecera
print(datos.head(5))
print(datos.columns)

#exportar datos
fichero = 'D:\workspace\WorkspaceTutorialCienciaDatos\datos\precios_cochesCopia.csv'
datos.to_csv(fichero)

# otros formatos de archivos
#datos.to_json(fichero)
#datos.to_excel(fichero)
#datos.to_sql(fichero)

#pd.read_json(fichero)
# _excel(fichero)
# _sql(fichero)