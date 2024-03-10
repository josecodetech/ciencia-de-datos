from datetime import datetime

import joblib
from arboles_regresion import *

def predecir(modelo):
    tienda = input('Dime la tienda : ')
    año = int(input('Dime el año : '))
    mes = int(input('Dime el mes : '))
    dia = int(input('Dime el dia : '))
    es_festivo = input('Dime si es festivo : (Si/No) ')
    fecha = f'{año}/{mes}/{dia}'
    fecha = datetime.strptime(fecha, '%Y/%m/%d')
    dia_semana = fecha.weekday()
    
    tiendas = {'Tienda_00': 0, 'Tienda_01': 1, 'Tienda_02': 2, 'Tienda_03': 3, 'Tienda_04': 4, 'Tienda_05': 5 }
    tienda_num = tiendas[tienda]
    festivos = {'No': 0, 'Si': 1}
    festivo_num = festivos[es_festivo]
    estacion = obtener_estacion(mes)
    estaciones = {'Invierno':0,'Primavera':1,'Verano':2,'Otoño':3}
    estacion_num = estaciones[estacion]
    datos = {
        'TIENDA': [tienda_num,],
        'AÑO': [año,],
        'MES': [mes,],
        'DIA': [dia,],
        'DIA_SEMANA': [dia_semana,],
        'FESTIVO':[festivo_num,],
        'ESTACION':[estacion_num,]
    }
    df_datos = pd.DataFrame(datos)
    prediccion = modelo.predict(df_datos)
    return df_datos, prediccion
def cargar_modelo(nombre='modelo_rf.joblib'):
    archivo = f"./modelos/{nombre}"
    modelo = joblib.load(archivo)
    return modelo
if __name__ == '__main__':
    modelo = cargar_modelo()
    datos, prediccion = predecir(modelo)
    print(prediccion)
    datos['PREDICCION'] = prediccion
    grabar_datos(datos,'prediccion.csv')