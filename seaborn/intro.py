import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn tiene datasets de práctica incluidos
df = sns.load_dataset("tips")
# print(df.head())
# print(df.shape)

# Matplotlib básico
# plt.figure(figsize=(8,5))
# plt.scatter(df["total_bill"], df["tip"])
# plt.title("Cuenta vs Propina - Matplotlib")
# plt.show()

# Seaborn equivalente
# plt.figure(figsize=(8,5))
# sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
# plt.title("Cuenta vs Propina - Seaborn")
# plt.show()

# # 1. Distribución de una variable
# plt.figure(figsize=(8,5))
# sns.histplot(data=df, x="total_bill", kde=True)
# plt.title("Distribución de cuentas")
# plt.show()

# # 2. Comparar distribuciones entre grupos
# plt.figure(figsize=(8,5))
# sns.boxplot(data=df, x="day", y="total_bill")
# plt.title("Cuentas por día de la semana")
# plt.show()

# # 3. Mapa de correlación
# plt.figure(figsize=(8,6))
# sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm")
# plt.title("Correlación entre variables")
# plt.show()

# Boxplot que compare las propinas (tip) entre fumadores y no fumadores (smoker)
plt.figure(figsize=(10,5))
sns.boxplot(data=df,x="smoker",y="tip")
plt.title("Promedio de propina: Fumadores vs No Fumadores")
plt.show() #Se observa que los no fumadores dejan propinas de mayor valor por los outliders y porque la caja de los fumadores Q3 es pequeño y Q1 es grande quiere decir que las propinas son bajas

# Scatterplot de cuenta vs propina separado por día (hue="day")
plt.figure(figsize=(10,5))
sns.scatterplot(data=df,x="total_bill", y="tip", hue="day")
plt.title("Cuenta vs Propina")
plt.show() #Hay bastantes puntos la mayoría se concentra en un rango de total_bill aprox de 7 a 23 con una propina similar, luego una distribución, los sábados hay propinas altas y gasto alto. No sabría que información valiosa rescatar de este gráfico. 

# Histograma de propinas con kde=True separado por género (hue="sex")
plt.figure(figsize=(10,5))
sns.histplot(data=df, x="tip", kde=True, hue="sex" )
plt.title("Propina por género")
plt.show() #El hombre deja más propina que la mujer en general.