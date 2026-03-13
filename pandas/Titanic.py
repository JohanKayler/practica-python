import pandas as pd

df = pd.read_csv("pandas/train.csv")
print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum()) #Eso te muestra exactamente cuántos nulos tiene cada columna.

# Eliminar filas con nulos
df_sin_nulos = df.dropna()
print(df_sin_nulos.shape)

# Rellenar nulos con el promedio
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())

# Eliminar una columna inútil
df = df.drop(columns=["Cabin"])
print(df.columns)

#subset=["Embarked"] le dice a Pandas que solo elimine filas donde Embarked sea nulo, no todo el DataFrame.
df = df.dropna(subset=["Embarked"])
print(df.isnull().sum())

# ¿Cuántos pasajeros sobrevivieron y cuántos no? (columna Survived: 1 = sí, 0 = no)
# ¿Cuál fue el promedio de edad de los pasajeros?
# ¿Cuántos pasajeros había en cada clase? (columna Pclass)

print(df["Survived"].value_counts())