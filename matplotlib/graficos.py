import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("pandas/train.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop(columns=["Cabin"])
df = df.dropna(subset=["Embarked"])

#Gráfico de barras 
supervivencia_genero = df.groupby("Sex")["Survived"].mean()
supervivencia_genero.plot(kind="bar", color=["steelblue", "salmon"])
plt.title("Tasa de supervivencia por genero")
plt.ylabel("Tasa de supervivencia")
plt.xticks(rotation=0)
plt.show()

# Histograma de edades
df["Age"].plot(kind="hist", bins=20, color="steelblue", edgecolor="black")
plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.show()

#Supervivencia por clase
df.groupby("Pclass")["Survived"].mean().plot(kind="bar", color="coral")
plt.title("Tasa de supervivencia por clase")
plt.xlabel("Clases")
plt.ylabel("Tasa de supervivencia")
plt.xticks(rotation=0)
plt.show()

#Tarifa pagada de sobrevivientes vs fallecidos 
df.groupby("Survived")["Fare"].mean().plot(kind="bar", color=["salmon", "steelblue"])
plt.title("Tarifa promedio: Sobrevivientes vs Fallecidos")
plt.ylabel("Tarifa promedio")
plt.xticks(rotation=0)
plt.show()

#Promedio de edad por género
df.groupby("Sex")["Age"].mean().plot(kind="bar", color=["purple", "steelblue"])
plt.title("Promedio de edad por género")
plt.ylabel("Promedio de edad")
plt.xticks(rotation=0)
plt.show()