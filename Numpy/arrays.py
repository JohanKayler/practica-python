# import numpy as np

# # Crear arrays especiales
# print(np.zeros((3, 3)))      # matriz de ceros
# print(np.ones((2, 4)))       # matriz de unos
# print(np.arange(0, 20, 2))   # del 0 al 20 de 2 en 2
# print(np.linspace(0, 1, 5))  # 5 números entre 0 y 1
# print(np.random.randint(1, 100, (3, 3)))  # matriz 3x3 de números aleatorios

# Crea una matriz de 5x5 de números aleatorios entre 1 y 50. Luego:
# Imprime el promedio de toda la matriz
# Imprime el valor máximo
# Imprime solo los valores mayores a 25

import numpy as np

matriz = np.random.randint(1,50,(5,5))

print(matriz)
print(matriz.mean())
print(matriz.max())
print(matriz[matriz>=25])

