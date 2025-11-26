import pandas as pd

df = pd.read_csv("mtcars.csv")

first_col = df.columns[0]
first_col_is_model = df[first_col].dtype == object and df[first_col].nunique() == len(df)

if first_col_is_model:
    df = df.set_index(first_col)
    df.index.name = "model"

if "Lotus Europa" in df.index:
    lotus = df.loc["Lotus Europa"]
else:
    lotus = "Lotus Europa not found in this dataset."

print(lotus)
