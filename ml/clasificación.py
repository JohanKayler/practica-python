import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

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

from sklearn.ensemble import RandomForestClassifier

modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)

y_pred_rf = modelo_rf.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

importancias = pd.Series(modelo_rf.feature_importances_, )
importancias.sort_values().plot(kind="barh", color="steelblue")
plt.title("Importancia de cada feature")
plt.show()