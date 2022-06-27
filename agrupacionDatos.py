# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:42:37 2022

@author: Jose
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fichero = 'D:\workspace\WorkspaceTutorialCienciaDatos\datos\precios_coches.csv'


datos = pd.read_csv(fichero)



print(datos.columns)

titulos_cabecera = ['indice','nombre','localizacion','año','kilometros recorridos','combustible','transmision','tipo propietario', 'kilometraje','motor','potencia','asientos','precio']

datos.columns = titulos_cabecera
print(datos.head(5))
print(datos.columns)

intervalo = np.linspace(min(datos['kilometros recorridos']),max(datos['kilometros recorridos']),4)
nombre_grupos = ['pocos','normal','muchos']
datos['kilometros agrupados']=pd.cut(datos['kilometros recorridos'],intervalo,labels=nombre_grupos,include_lowest=True)
print(datos['kilometros agrupados'])

plt.hist(datos['kilometros recorridos'],bins=intervalo, rwidth=0.9, color='#991')
plt.title('Histograma kilometros recorridos')
plt.xlabel('Kilometros')
plt.ylabel('Frecuencia')
plt.show()


     