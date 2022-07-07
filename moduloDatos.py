import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split


def crearDataSet(filas, columnas, nombre_columnas, inicial=0, final=1000,):
    datos = pd.DataFrame(np.random.randint(
        inicial, final, (filas, columnas)), columns=nombre_columnas)
    return datos


def cargaDatos(ruta, fichero, separador=','):
    datos = pd.read_csv(ruta+fichero, sep=separador)
    return datos


def dameColumnas(datos):
    return datos.columns


def cambiaColumnas(datos, columnas):
    datos.columns = columnas
    return datos


def renombrarColumna(datos, columna, cambio):
    datos.rename(columns={columna: cambio}, inplace=True)
    return datos


def guardarDatos(datos, ruta, fichero):
    datos.to_csv(ruta+fichero)
    return True


def cambiaNombreIndice(datos, nombre='indice'):
    datos.index.name = nombre
    return datos


def reemplazarNulos(columna):
    media = columna.mean()
    columna.replace(np.nan, media, inplace=True)
    return columna


def cambiaTipo(columna, tipo='float64'):
    #columna = columna.astype(tipo)
    #datos['potencia'] = pd.to_numeric(datos['potencia'],errors = 'coerce')
    columna = pd.to_numeric(columna, errors='coerce')
    return columna


def normalizaColumna(columna):
    columna = columna/columna.max()
    return columna


def obtenerDummies(columna):
    columnas = pd.get_dummies(columna)
    return columnas


def agruparDatos(datos, columna):
    datos_agrupados = datos.groupby(columna, as_index=False)
    return datos_agrupados

# visualizacion de datos


def graficaBoxPlot(columna, titulo=''):
    plt.boxplot(columna)
    plt.title(titulo)
    plt.show()


def graficaScatter(x, y, titulo='', etiquetaX='X', etiquetaY='Y'):
    plt.scatter(x, y)
    plt.title(titulo)
    plt.xlabel(etiquetaX)
    plt.ylabel(etiquetaY)
    plt.show()


# Regresiones
def regresionLineal(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)

    lm = LinearRegression()

    lm.fit(X_train, y_train)
    return lm


def damePrediccionRL(lm, X):
    prediccion = lm.predict(X)
    #print(lm.score(X, y))
    return prediccion

# Estadisticos
def dameEstadisticos(datos, tipo='numerico'):
    """tipo numerio o todos"""
    if tipo == 'numerico':
        return datos.describe()
    else:
        return datos.describe(include='all')


def coeficientePearson(columna1, columna2):
    pearson_coef, p_valor = stats.pearsonr(columna1, columna2)
    return pearson_coef, p_valor
def errorCuadratico(y_real, prediccion):
    ECM = metrics.mean_squared_error(y_real, prediccion)
    #print(ECM)
    return ECM
def rCuadrado(y_real, prediccion):
    r_cuadrado = metrics.r2_score(y_real, prediccion)
    #print(r_cuadrado)
    return r_cuadrado



if __name__ == '__main__':
    ruta = 'D:\\workspace\\WorkspaceTutorialCienciaDatos\\datos\\'
    fichero = 'precios_coches.csv'
    datos = cargaDatos(ruta, fichero)
    print(datos.head(5))
    print(dameColumnas(datos))
    #graficaBoxPlot(datos['Kilometers_Driven'], 'Kilometros')
    datos = crearDataSet(100, 5, ['A', 'B', 'C', 'D', 'E'])
    print(datos.head())
    X = datos['A']
    y = datos['E']
    graficaScatter(X, y, titulo='Pruebas')
    print(coeficientePearson(X, y))
    print(X.shape)
    X = np.array(X).reshape(1, -1).T
    print(X.shape)
    print(y.shape)
    lm = regresionLineal(X, y)
    prediccion = damePrediccionRL(lm, X)
    print(y, prediccion)
    print(rCuadrado(y,prediccion))
