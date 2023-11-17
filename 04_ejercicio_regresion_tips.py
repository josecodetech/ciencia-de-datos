import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

tips_datos = sns.load_dataset('tips')
df = pd.DataFrame(tips_datos)

# variable predictora (X) y variable objetivo (Y)
X = df[['total_bill']]
y = df['tip']

# divivir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

# creamos el modelo
model = LinearRegression()

# Entrenar el Modelo
model.fit(X_train, y_train)

# Predicción del Modelo
y_pred = model.predict(X_test)

# obtenemos los coeficientes (pendiente e interseccion) y = a + bx   propina = 0.107 + 0.925 * total cuenta
print('Pendiente : ', model.coef_[0])
print('Interseccion : ', model.intercept_)

# evaluar rendimiento del modelo
print('Error cuadratico medio (MSE) : ', mean_squared_error(y_test, y_pred))
print('Coeficiente de determinacion (R^2) : ', r2_score(y_test, y_pred))

# visualizamos regresion y datos reales
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth = 2)
plt.title('Regresion lineal: Venta total vs Propina')
plt.xlabel('Venta total')
plt.ylabel('Propina')
plt.show()

# creamos nuevos datos
nuevos_datos = pd.DataFrame({'total_bill':[30,40,50,60,70]})
# realizamos predicciones
predicciones = model.predict(nuevos_datos)
# mostramos predicciones
for i, prediccion in enumerate(predicciones):
    print(f"Venta Total: {nuevos_datos['total_bill'][i]} - Prediccion de propina : {prediccion}")
