import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")
# print(df.head())

df["porcentaje_propina"] = df["tip"]/df["total_bill"]*100
df["es_fin_de_semana"] = (df["day"] == "Sun") | (df["day"] == "Sat")
df["propina_por_persona"] = df["total_bill"]/df["size"]
# print(df.head())

from sklearn.preprocessing import LabelEncoder

# Label Encoding
le = LabelEncoder()
df["sex_encoded"] = le.fit_transform(df["sex"])

# One Hot Encoding
df_ohe = pd.get_dummies(df, columns=["day"], prefix="dia")

# Label Encoding a smoker y time
df["smoker_encoding"] = le.fit_transform(df["smoker"])
df["time_encoding"] = le.fit_transform(df["time"])
#One Hot Encoding a sex
df_ohe = pd.get_dummies(data=df, columns=["sex"])
print(df_ohe.head())