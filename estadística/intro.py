import numpy as np

datos = np.array([23, 25, 28, 22, 30, 27, 24, 29, 26, 25])

# print("Media:", np.mean(datos))
# print("Mediana:", np.median(datos))
# print("Desviación estándar:", np.std(datos))
# print("Varianza:", np.var(datos))
# print("Mínimo:", np.min(datos))
# print("Máximo:", np.max(datos))


# horas_estudio = np.array([2, 4, 6, 8, 10, 3, 7, 5, 9, 1])
# notas          = np.array([45, 60, 75, 85, 95, 50, 80, 70, 90, 35])

# correlacion = np.corrcoef(horas_estudio, notas)
# print(correlacion)

# temperatura = np.array([30, 32, 35, 28, 33, 31, 29, 34, 36, 27])
# ventas_helado = np.array([200, 220, 260, 180, 240, 210, 190, 250, 270, 170])

# correlacion1= np.corrcoef(temperatura,ventas_helado)
# print(correlacion1)


import matplotlib.pyplot as plt

# Distribución normal
datos_normales = np.random.normal(loc=170, scale=10, size=1000)
# loc = promedio, scale = desviación estándar, size = cantidad de datos

# plt.hist(datos_normales, bins=30, color="steelblue", edgecolor="black")
# plt.title("Distribución normal - Alturas")
# plt.xlabel("Altura (cm)")
# plt.ylabel("Frecuencia")
# plt.show()

# print("Promedio:", np.mean(datos_normales))
# print("Std:", np.std(datos_normales))
# print(datos_normales)


datos = np.array([22, 24, 23, 25, 26, 24, 23, 25, 100, 22, 24, 26, 23])

# plt.boxplot(datos)
# plt.title("Boxplot - detectando outliers")
# plt.show()

print("Promedio:", np.mean(datos))
print("Mediana:", np.median(datos))

Q1 = np.percentile(datos, 25)
Q3 = np.percentile(datos, 75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = datos[(datos < limite_inferior) | (datos > limite_superior)]
# print("Outliers:", outliers)

from scipy import stats

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
# plt.show()



def predecir_nota(horas):
    nota = 6.6 * horas + 31
    return nota

print(predecir_nota(11))
print(predecir_nota(12))
print(predecir_nota(15))