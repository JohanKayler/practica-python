from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import numpy as np

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

modelo = LinearRegression()
scores = cross_val_score(modelo, X, y, cv=5, scoring="r2")

# print("R² por fold:", scores)
# print("R² promedio:", np.mean(scores))
# print("Desviación estándar:", np.std(scores))

from sklearn.ensemble import RandomForestRegressor

modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
scores_rf = cross_val_score(modelo_rf, X, y, cv=5, scoring="r2")

print("RF R² por fold:", scores_rf)
print("RF R² promedio:", np.mean(scores_rf))
print("RF Std:", np.std(scores_rf))