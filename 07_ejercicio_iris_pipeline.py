from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
# carga del dataset
iris = load_iris()
X, y = iris.data, iris.target

# separación en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# crear el pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])

# entrenamiento del modelo
pipeline.fit(X_train, y_train)
# evaluacion del modelo
valoracion = pipeline.score(X_test, y_test)
print(f"Valoracion: {valoracion}")
# guardar el modelo
joblib.dump(pipeline, '07_iris_pipeline.pkl')
# cargar y usar el modelo
modelo_cargado = joblib.load('07_iris_pipeline.pkl')
# hacer una prediccion
ejemplo = X_test[0].reshape(1,-1)
print('Dato de ejemplo usado para predecir: ')
print(ejemplo)
prediccion = modelo_cargado.predict(ejemplo)
print("Prediccion: ")
print(prediccion)
print(f"Prediccion: {iris.target_names[prediccion]}")