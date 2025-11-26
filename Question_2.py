import pandas as pd

df = pd.read_csv("mtcars.csv")

if "hp" in df.columns:
    df_no_hp = df.drop(columns=["hp"])
else:
    df_no_hp = df

print(df_no_hp)
