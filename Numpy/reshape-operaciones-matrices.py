# import numpy as np

# arr = np.arange(1, 13)        # [1, 2, 3, ... 12]
# matriz = arr.reshape(3, 4)    # convierte a matriz 3x4
# print(matriz)

# # Operaciones entre matrices
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# print(a + b)           # suma elemento por elemento
# print(a * b)           # multiplicación elemento por elemento
# print(np.dot(a, b))    # multiplicación matricial (la usarás en ML)

# Ejercicio:
# Crea un array del 1 al 24 y conviértelo a una matriz de 4x6. 
# Luego multiplícala matricialmente por su transpuesta (matriz.T). 
# Imprime el resultado y el shape del resultado.

import numpy as np

lista = np.arange(1,25)
matriz = lista.reshape(4,6)
matriz_transpuesta = matriz.T
multiplicacion = np.dot(matriz,matriz_transpuesta)
print(multiplicacion)
print(multiplicacion.shape)