import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Cargar y limpiar datos
df = pd.read_csv("pandas/train.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop(columns=["Cabin"])
df = df.dropna(subset=["Embarked"])

# Convertir género a número (ML solo entiende números)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# Seleccionar features y target
X = df[["Pclass", "Sex", "Age", "Fare"]]
y = df["Survived"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Evaluar
y_pred = modelo.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

import numpy as np

# [Pclass, Sex, Age, Fare]
pasajeros = np.array([
    [3, 0, 25, 7.25],   # hombre joven, 3ra clase, tarifa baja
    [1, 1, 35, 100.0],  # mujer adulta, 1ra clase, tarifa alta
    [2, 0, 45, 30.0],   # hombre mayor, 2da clase
])

predicciones = modelo.predict(pasajeros)
print(predicciones)
print(classification_report(predicciones))