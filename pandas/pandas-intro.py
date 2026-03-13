import pandas as pd

data = {
    "nombre": ["Johan", "Maria", "Carlos", "Ana"],
    "edad": [17, 23, 19, 25],
    "ciudad": ["Callao", "Lima", "Miraflores", "Surco"],
    "nota": [18, 15, 12, 20]
}

df = pd.DataFrame(data)
# print(df)
# print(df.shape)
# print(df.dtypes)
# print(df.describe())

# print(df["nombre"])           # una columna
# print(df[["nombre", "nota"]]) # varias columnas
# print(df[df["nota"] >= 15])   # filtrar filas por condición
# print(df.sort_values("nota")) # ordenar por columna
# print(df["nota"].mean())      # promedio de una columna

# Agrega una columna "aprobado" que sea True si la nota 
# es mayor o igual a 11 y False si no.
# Imprímela junto al nombre y la nota.

#FORMA NO OPTIMA 
# import numpy as np
# notas = np.array(data["nota"])
# data["aprobado"] = notas>=11
# df1=pd.DataFrame(data)
# print(df1[["nombre","nota","aprobado"]])

#FORMA ÓPTIMA
df["aprobados"] = df["nota"]>=11
print(df[["nombre","nota","aprobados"]])
