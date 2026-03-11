import numpy as np

# arr = np.array([4, 7, 2, 9, 1, 5])

# print(np.sum(arr))      # suma total
# print(np.mean(arr))     # promedio
# print(np.max(arr))      # máximo
# print(np.min(arr))      # mínimo
# print(np.sort(arr))     # ordenar
# print(np.std(arr))      # desviación estándar

# Tienes las notas de 8 alumnos: [14, 18, 11, 9, 16, 13, 20, 7]
# Con NumPy en pocas líneas:
# Calcula el promedio
# Encuentra la nota máxima y mínima
# Cuántos alumnos aprobaron (nota >= 11) — para esto usa: arr[arr >= 11]
# Imprime las notas ordenadas de menor a mayor

import numpy as np
notas = np.array([14, 18, 11, 9, 16, 13, 20, 7])

print(np.mean(notas))
print(np.max(notas))
print(np.min(notas))
notas_aprobados=notas[notas >= 11]
print(notas_aprobados)
print(f"Aprobaron {len(notas_aprobados)} alumnos")
print(np.sort(notas))
print(np.sort(notas)[::-1]) #Invierte el array


