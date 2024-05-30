import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import classification_report, accuracy_score

iris = load_iris()
X = iris.data
y = iris.target
caracteristicas = iris.feature_names
etiquetas = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
# crear y entrenar
modelo_arbol = DecisionTreeClassifier(random_state=2)
modelo_arbol.fit(X_train, y_train)
y_pred = modelo_arbol.predict(X_test)
# evaluar
print("Accuracy: ",accuracy_score(y_test, y_pred))
print("\nClassification Report: \n", classification_report(y_test, y_pred,target_names=etiquetas))
# visualizar el arbol
plt.figure(figsize=(20, 10))
plot_tree(modelo_arbol, feature_names=caracteristicas, class_names=etiquetas, filled=True)
plt.title("Arbol de decision - Dataset Iris")
plt.show()
