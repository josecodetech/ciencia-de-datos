import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

datos = load_breast_cancer()
X = pd.DataFrame(datos.data, columns=datos.feature_names)
y = pd.Series(datos.target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train_escalado = scaler.fit_transform(X_train)
X_test_escalado = scaler.transform(X_test)
# print(X_train_escalado)
# modelo knn
knn_modelo = KNeighborsClassifier(n_neighbors=5)
knn_modelo.fit(X_train_escalado, y_train)
# print(knn_modelo)
knn_pred = knn_modelo.predict(X_test_escalado)
knn_accuracy = accuracy_score(y_test, knn_pred)
print("Accuracy del modelo KNN: ",knn_accuracy)
print("Report del modelo: ")
print(classification_report(y_test, knn_pred))
# modelo random forest
rf_modelo = RandomForestClassifier(n_estimators=100, random_state=42)
rf_modelo.fit(X_train_escalado, y_train)
rf_pred = rf_modelo.predict(X_test_escalado)
rf_accuracy = accuracy_score(y_test, rf_pred)
print('*'*50)
print("Accuracy del modelo Random Forest: ", rf_accuracy)
print("Report del modelo: ")
print(classification_report(y_test, rf_pred))
# seleccion mejor modelo
mejor_modelo = knn_modelo if knn_accuracy > rf_accuracy else rf_modelo
print('*'*50)
print("El mejor modelo es: ",mejor_modelo)
print('*'*50)
joblib.dump(mejor_modelo, "mejor_modelo.pkl")
# carga del modelo
modelo_cargado = joblib.load("mejor_modelo.pkl")
pred = modelo_cargado.predict(X_test_escalado)
comparacion = pd.DataFrame({'Real':y_test, 'Prediccion':pred})
print("Comparacion valores reales y predichos:")
print(comparacion)