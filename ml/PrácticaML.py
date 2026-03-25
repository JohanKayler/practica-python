# Ejercicio Práctico — Machine Learning 
# Dataset: Diabetes (sklearn)

from sklearn.datasets import load_diabetes
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import numpy as np

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

# Resuelve lo siguiente:

# Explora el dataset. ¿Cuántas filas y columnas tiene? ¿Hay valores nulos? ¿Cómo se distribuyen los datos?
print(df.info())
import matplotlib.pyplot as plt
df.hist() #Creo un histograma de cada columna de df
plt.tight_layout() #ajusta automáticamente los espacios entre subgráficos para que no se superpongan.
plt.show()
# 442 filas, 11 columnas
# Sin valores nulos
# Datos normalizados entre -1 y 1
# La mayoría siguen distribución normal
# Sex es categórica con dos valores

# Selecciona las features que consideres más relevantes para predecir el target. Justifica tu elección.
print(df.corr()["target"].sort_values(ascending=False)) #Identifico que features son más relevantes para precedir el target

# Divide los datos en entrenamiento (80%) y prueba (20%).
x = df[["bmi","s5","bp","s4","s6","s3"]]
y = df["target"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Entrena un modelo de Regresión Lineal y evalúalo con R² y MSE.
modelo = LinearRegression()
modelo.fit(x_train,y_train)

#Predecir
y_pred = modelo.predict(x_test)
#Evaluando
print("R²:", r2_score(y_test, y_pred))
print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))

# Entrena un modelo de Random Forest con 100 árboles y evalúalo con los mismos métricas.
modelo_rf= RandomForestRegressor(n_estimators=100, random_state=42)
modelo_rf.fit(x_train,y_train)

#Predecir
y_pred_rf= modelo_rf.predict(x_test)

#Evaluando
print("R²:", r2_score(y_test, y_pred_rf))
print("MSE:", mean_squared_error(y_test, y_pred_rf))

# Compara ambos modelos. ¿Cuál funcionó mejor y por qué crees que fue así?

# Usa el mejor modelo para predecir el target de 3 pacientes nuevos inventados por ti. (-0.1,0.15)
pacientes = np.array([[0.08, -0.02, 0.02, 0.10, -0.02, 0.09],
                      [-0.1, 0.11, 0.9, 0.6, -0.05, 0.1],
                      [0.03, 0.04,-0.02,0.04,0.15,0.1]
])

predicciones=modelo.predict(pacientes)
print(predicciones)