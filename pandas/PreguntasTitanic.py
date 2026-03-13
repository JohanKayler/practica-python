import pandas as pd

df = pd.read_csv("pandas/train.csv")

#Revisando información
print(df.info())

#Agregando el promedio en datos nulos en la columna edad
df["Age"] = df["Age"].fillna(df["Age"].mean())

#Eliminando columna inutil
df = df.drop(columns=["Cabin"])

#Eliminando filas nulas
df = df.dropna(subset=["Embarked"])

#Verificando que los datos estén limpios
print(df.isnull().sum())

# ¿Cuántos pasajeros sobrevivieron y cuántos no? (columna Survived: 1 = sí, 0 = no)
dato_supervivenvia = df["Survived"].value_counts()
print(dato_supervivenvia) #De aca se observa que sobrevivieron 340 y 549 fallecieron

# ¿Cuál fue el promedio de edad de los pasajeros?
promedio_edad = df["Age"].mean()
print(promedio_edad) #Promedio igual a 29.65 años

# ¿Cuántos pasajeros había en cada clase? 
pasajerosEnCadaClase = df["Pclass"].value_counts()
print(pasajerosEnCadaClase) #En primera clase 214, en segunda clase 184 y en tercera clase 491.

# ¿Cuál fue la tasa de supervivencia por género? (columna Sex)
TasaSupervivenciaPorGenero = df.groupby("Sex")["Survived"].mean()
print(TasaSupervivenciaPorGenero)

# ¿El promedio de edad de los que sobrevivieron vs los que no sobrevivieron?
PromedioEdadSupervivencia = df.groupby("Survived")["Age"].mean()
print(PromedioEdadSupervivencia)

# ¿Cuántos menores de 18 años había en el barco?
datosMenoresEdad = df[df["Age"] < 18]
print(len(datosMenoresEdad))

# ¿Cuál fue la tasa de supervivencia por clase (Pclass)?
TasaSupervivenciaPorClase = df.groupby("Pclass")["Survived"].mean()
print(TasaSupervivenciaPorClase)

# ¿Cuál fue el promedio de edad por clase?
PromedioEdadPorClase = df.groupby("Pclass")["Age"].mean()
print(PromedioEdadPorClase)

# ¿Cuál fue la tarifa promedio pagada (columna Fare) por los sobrevivientes vs los que no sobrevivieron?
TarifaPromedio = df.groupby("Survived")["Fare"].mean()
print(TarifaPromedio)

#CONCLUSIONES 
# 1. Las mujeres tuvieron una tasa de supervivencia del 74% vs 18% de los hombres.
#   Esto confirma la política "mujeres y niños primero".

# 2. La clase social fue determinante: 1ra clase sobrevivió ~63%, 
#   3ra clase solo ~24%. El dinero aumentaba las chances de sobrevivir.

# 3. Los sobrevivientes pagaron en promedio el doble de tarifa,
#   lo que se relaciona directamente con el punto anterior.

# 4. Había 113 menores de 18 años a bordo.

# 5. El pasajero promedio tenía ~29 años.