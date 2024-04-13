import joblib
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer


propinas = sns.load_dataset('tips')
print("Estadisticas basicas del conjunto de datos: ")
print(propinas.describe())
print("Informacion basica del conjunto de datos: ")
print(propinas.info())
propinas_limpias = propinas.dropna().drop_duplicates()
print("Informacion basica del conjunto de datos limpio: ")
print(propinas_limpias.info())
sns.heatmap(propinas_limpias.corr(), annot=True, cmap='coolwarm',fmt=".2f")
plt.title("Correlacion entre variables")
plt.show()
X = propinas_limpias.drop('tip', axis=1)
X = X.drop('time',axis=1)
y = propinas_limpias['tip']
modelo = Pipeline([
    ('preprocesamiento',ColumnTransformer(
        [
           ('scaler',StandardScaler(),['total_bill','size']),
           ('onehot', OneHotEncoder(), ['day', 'smoker', 'sex']) 
        ],remainder='passthrough')),
    ('regressor',RandomForestRegressor())]) 
scores = cross_val_score(modelo, X, y, cv=5, scoring='neg_mean_squared_error')
rmse_scores = np.sqrt(-scores)
print("\nResultados de la validacion cruzada:")
print("RMSE medio:", rmse_scores.mean())
print("Desviacion estandar:", rmse_scores.std())
modelo.fit(X,y)
fichero = 'modelo_random_forest.pkl'
joblib.dump(modelo, fichero)
print("Modelo guardado en fichero:", fichero)
modelo_cargado = joblib.load(fichero)
X_nuevos = X.head(5)
predicciones = modelo_cargado.predict(X_nuevos)
print("\nPredicciones para los primeros 5 registros:")
print(X_nuevos)
print(predicciones)
