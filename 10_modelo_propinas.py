import joblib

modelo = joblib.load('propinas.pkl')

datos = [[50.00,4],[30.00,2],[40.00,3]]
predicciones = modelo.predict(datos)
for i, pred in enumerate(predicciones):
    print(f'Prediccion para {datos[i]}: {pred:.2f}')