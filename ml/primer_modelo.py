import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Datos
horas_estudio = np.array([1,2,3,4,5,6,7,8,9,10,3,7,5,2,8,4,6,9,1,10]).reshape(-1, 1)
notas = np.array([35,45,50,60,65,70,78,85,90,95,52,80,68,44,88,61,73,91,38,96])

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(horas_estudio, notas, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train,y_train)

# Predecir
y_pred = modelo.predict(X_test)

# Evaluar
print("R²:", r2_score(y_test, y_pred))
print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))
print("Pendiente:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

# Predecir para un estudiante nuevo
horas_nuevas = np.array([[7]])
print("Predicción para 7 horas:", modelo.predict(horas_nuevas)[0])
print(modelo())