import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import joblib

propinas = sns.load_dataset('tips')
print(propinas.head())
print(propinas.info())
print(propinas.describe())
sns.pairplot(propinas)
plt.show()
X = propinas[['total_bill', 'size']]
y = propinas['tip']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=40)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
# evaluacion modelo
train_score = modelo.score(X_train, y_train)
test_score = modelo.score(X_test, y_test)
print(f"Coeficiente de determinacion en conjunto de entrenamiento: {train_score:.2f}")
print(f"Coeficiente de determinacion en conjunto de pruebas: {test_score:.2f}")
# guardar modelo
joblib.dump(modelo, 'propinas.pkl')
print("Modelo guardado, como propinas.pkl")
