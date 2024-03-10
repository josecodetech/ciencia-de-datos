from joblib import dump, load
import pandas as pd
import datetime as dt
from datetime import datetime
import os
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def carga_datos(nombre):
    directorio = 'datos'
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    fichero = os.path.join(directorio,nombre)
    datos = pd.read_csv(fichero)
    return datos
def grabar_datos(df,nombre='ventas.csv'):
    directorio = 'datos'
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    fichero = os.path.join(directorio,nombre)
    df.to_csv(fichero, index=False)
    print("Fichero guardado en: ", fichero)
def es_festivo(fecha):
    festivos = ['01-01','06-01','28-02','01-05','15-08','12-10','01-11','06-12','08-12','25-12']
    fecha_sin_año = fecha.strftime('%d-%m') #ignoramos año
    dia_semana = fecha.weekday() # 0 lunes, 1 martes ...
    if fecha_sin_año in festivos or dia_semana == 6:
        return 1 # retorna festivo, True o 1
    else:
        return 0 
def obtener_estacion(mes):
    if mes in (1,2,12):
        return 'Invierno'
    elif mes in (3,4,5):
        return 'Primavera'
    elif mes in (6,7,8):
        return 'Verano'
    else:
        return 'Otoño'
def prepara_fechas(df):
    df['AÑO'] = (df['FECHA']).str[:4]
    df['MES'] = (df['FECHA']).str[5:7]
    df['DIA'] = (df['FECHA']).str[8:10]
    df.drop('FECHA', axis=1, inplace=True)
    df['FECHA'] = df['AÑO']+'-'+df['MES']+'-'+df['DIA']
    df['FECHA'] = pd.to_datetime(df['FECHA'])
    df['DIA_SEMANA'] = df['FECHA'].dt.dayofweek
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    df['NOMBRE_DIA_SEMANA'] = df['FECHA'].dt.dayofweek.apply(lambda x: dias_semana[x])
    df['FESTIVO'] = df['FECHA'].apply(es_festivo)
    df['ESTACION'] = df['MES'].apply(obtener_estacion)
    return df
def prepara_datos_modelo(df):
    df_modelo = df[['TIENDA','TOTAL','AÑO','MES','DIA','DIA_SEMANA','FESTIVO','ESTACION']].copy()
    mapeo_estaciones = {'Invierno':0,'Primavera':1,'Verano':2,'Otoño':3}
    df_modelo['ESTACION'] = df_modelo['ESTACION'].map(mapeo_estaciones)
    mapeo_tiendas = {'Tienda_00': 0, 'Tienda_01': 1, 'Tienda_02': 2, 'Tienda_03': 3, 'Tienda_04': 4, 'Tienda_05': 5 } 
    df_modelo['TIENDA'] = df_modelo['TIENDA'].map(mapeo_tiendas)
    grabar_datos(df_modelo, 'ventas_modelo.csv') 
    X = df_modelo.drop('TOTAL', axis=1)
    y = df_modelo['TOTAL']
    return X, y
def entrenar_modelos(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
    # random forest
    modelo_rf = RandomForestRegressor(n_estimators=100, random_state=40)
    modelo_rf.fit(X_train, y_train)
    # regresion lineal
    modelo_rl = LinearRegression()
    modelo_rl.fit(X_train, y_train)
    dump(modelo_rf, './modelos/modelo_rf.joblib')
    dump(modelo_rl, './modelos/modelo_rl.joblib')
    return modelo_rf, modelo_rl, X_test, y_test
def evaluar_modelo(modelo, X_test, y_test, nombre_modelo):
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    plt.figure(figsize=(6,4))
    plt.scatter(y_test, y_pred, color='blue')
    plt.plot([y_test.min(),y_test.max()],[y_test.min(), y_test.max()],linestyle='--',color='red')
    plt.xlabel('Valor real')
    plt.ylabel('Prediccion')
    plt.title('Predicciones vs Valores reales')
    plt.grid(True)
    plt.show()
    print(f'Metricas del modelo {nombre_modelo}')
    print(f'Error cuadratico medio: {mse:.2f}')
    print(f'Coeficiente de determinacion: {r2:.2f}')
    return mse, r2
if __name__=='__main__':
    datos = carga_datos('ventas.csv')
    # print(datos.head())
    # grabar_datos(datos,'ventas.csv')
    datos = prepara_fechas(datos)
    # print(datos.head())
    X, y = prepara_datos_modelo(datos)
    # print(X)
    modelo_rf, modelo_rl, X_test, y_test = entrenar_modelos(X,y)
    mseRF, r2RF = evaluar_modelo(modelo_rf, X_test, y_test, 'Random Forest')
    mseLR, r2LR = evaluar_modelo(modelo_rl, X_test, y_test, 'Regresion Lineal')
    