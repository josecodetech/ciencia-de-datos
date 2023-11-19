# y = a + b*X
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split

# creamos conjunto de datos con gastos en publicidad y ventas
datos = {
    'Gasto_publicidad':[100,200,300,400,500,200,300,400,500,200,300,400,50],
    'Ventas': [800,900,700,600,500,900,700,600,500,900,700,600,500]
}
# creamos df
df = pd.DataFrame(data=datos)
# separamos variables en predictora y objetivo
X = df[['Gasto_publicidad']]
y = df['Ventas']
# entrenamiento y prueba 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
# modelo 
model = LinearRegression()
# entrenamos el modelo
model.fit(X_train, y_train)
# prediccion
y_pred = model.predict(X_test)
# coeficientes, pendiente e interseccion
# print('Coeficientes:', model.coef_)
print('Pendiente : ',model.coef_[0])
print('Interseccion : ',model.intercept_)
# evaluar el modelo
print('Error cuadratico medio (MSE) : ', mean_squared_error(y_test, y_pred))
print('Coeficiente de determinacion (R^2)', r2_score(y_test,y_pred))
# visualizamos
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test,y_pred,color='red',linewidth=2)
plt.title('Regresion lineal: Gasto en publicidad vs Ventas')
plt.xlabel('Gasto en publicidad')
plt.ylabel('Ventas')
plt.show()