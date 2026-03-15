import numpy as np

datos = np.array([23, 25, 28, 22, 30, 27, 24, 29, 26, 25])

print("Media:", np.mean(datos))
print("Mediana:", np.median(datos))
print("Desviación estándar:", np.std(datos))
print("Varianza:", np.var(datos))
print("Mínimo:", np.min(datos))
print("Máximo:", np.max(datos))


horas_estudio = np.array([2, 4, 6, 8, 10, 3, 7, 5, 9, 1])
notas          = np.array([45, 60, 75, 85, 95, 50, 80, 70, 90, 35])

correlacion = np.corrcoef(horas_estudio, notas)
print(correlacion)

temperatura = np.array([30, 32, 35, 28, 33, 31, 29, 34, 36, 27])
ventas_helado = np.array([200, 220, 260, 180, 240, 210, 190, 250, 270, 170])

correlacion1= np.corrcoef(temperatura,ventas_helado)
print(correlacion1)


import matplotlib.pyplot as plt

# Distribución normal
datos_normales = np.random.normal(loc=170, scale=10, size=1000)
# loc = promedio, scale = desviación estándar, size = cantidad de datos

plt.hist(datos_normales, bins=30, color="steelblue", edgecolor="black")
plt.title("Distribución normal - Alturas")
plt.xlabel("Altura (cm)")
plt.ylabel("Frecuencia")
plt.show()

print("Promedio:", np.mean(datos_normales))
print("Std:", np.std(datos_normales))
print(datos_normales)
