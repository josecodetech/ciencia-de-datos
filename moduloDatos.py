import pandas as pd
import numpy as np


def cargaDatos(ruta, fichero):
    datos = pd.read_csv(ruta+fichero)
    return datos


def dameColumnas(datos):
    return datos.columns


def cambiaColumnas(datos, columnas):
    datos.columns = columnas
    return datos


def renombrarColumna(datos, cambio):
    datos.rename(columns=cambio, inplace=True)
    return datos


def guardarDatos(datos, ruta, fichero):
    datos.to_csv(ruta+fichero)
    return True


def dameEstadisticos(datos, tipo='numerico'):
    """tipo numerio o todos"""
    if tipo == 'numerico':
        return datos.describe()
    else:
        return datos.describe(include='all')


def reemplazarNulos(datos, columna):
    media = datos[columna].mean()
    datos[columna].replace(np.nan, media, inplace=True)
    return datos


def cambiaTipo(columna, tipo='float64'):
    columna = columna.astype(tipo)
    return columna


def normalizaColumna(datos, columna):
    datos[columna] = datos[columna]/datos[columna].max()
    return datos


if __name__ == '__main__':
    ruta = 'D:\\workspace\\WorkspaceTutorialCienciaDatos\\datos\\'
    fichero = 'precios_coches.csv'
    datos = cargaDatos(ruta, fichero)
    print(datos.head(5))
    print(dameColumnas(datos))
    guardarDatos(datos, ruta, 'copia.csv')
    titulos_cabecera = ['indice', 'nombre', 'localizacion', 'año', 'kilometros recorridos', 'combustible',
                        'transmision', 'tipo propietario', 'kilometraje', 'motor', 'potencia', 'asientos', 'precio']
    cambiaColumnas(datos, titulos_cabecera)
    print(datos.columns)
    print(dameEstadisticos(datos))
    print(dameEstadisticos(datos, 'todos'))
    columna = datos['kilometros recorridos']
    columna = cambiaTipo(columna, 'int64')
    print(columna.dtype)
    print(columna)
    datos = renombrarColumna(datos, {'kilometros recorridos': 'kilometros'})
    print(datos.columns)
    datos = normalizaColumna(datos, 'kilometros')
    print(datos['kilometros'])
