#pip install faker
import pandas as pd
from faker import Faker
datos = {}
datos_ficticios = Faker()

def crear_datos(cantidad):
    datos = {}
    datos_ficticios = Faker()
    for i in range(cantidad):
        nombre = datos_ficticios.name()
        direccion = datos_ficticios.address()
        datos[nombre]=direccion
    return datos
def generar_df(diccionario):
    df = pd.DataFrame([[clave, diccionario[clave]] for clave in diccionario.keys()], columns=['nombre','direccion'])
    return df
def crear_csv(df, fichero='datos'):
    nombre_fichero = fichero+".csv"
    df.to_csv(nombre_fichero,encoding='utf-8')
if __name__=='__main__':
    datos =crear_datos(100)
    df = generar_df(datos)
    print(df.head())
    crear_csv(df,"pruebas")
    