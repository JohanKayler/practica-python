import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

datos = np.array([22, 24, 23, 25, 26, 24, 23, 25, 100, 22, 24, 26, 23])

plt.boxplot(datos)
plt.title("Boxplot - detectando outliers")
plt.show()

print("Promedio:", np.mean(datos))
print("Mediana:", np.median(datos))

Q1 = np.percentile(datos, 25)
Q3 = np.percentile(datos, 75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = datos[(datos < limite_inferior) | (datos > limite_superior)]
print("Outliers:", outliers)


horas_estudio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
notas = np.array([35, 45, 50, 60, 65, 70, 78, 85, 90, 95])

slope, intercept, r_value, p_value, std_err = stats.linregress(horas_estudio, notas)

print("Pendiente:", slope)
print("Intercepto:", intercept)
print("R²:", r_value**2)

# Línea de regresión
plt.scatter(horas_estudio, notas, color="steelblue", label="Datos reales")
plt.plot(horas_estudio, slope * horas_estudio + intercept, color="red", label="Línea de regresión")
plt.title("Horas de estudio vs Notas")
plt.xlabel("Horas de estudio")
plt.ylabel("Nota")
plt.legend()
plt.show()

def predecir_nota(horas):
    nota = 6.6 * horas + 31
    return nota

print(predecir_nota(11))
print(predecir_nota(12))
print(predecir_nota(15))