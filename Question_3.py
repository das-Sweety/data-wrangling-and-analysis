import pandas as pd

df = pd.read_csv("mtcars.csv")

cols = ["mpg", "hp", "vs", "am", "gear"]
print(df[cols])
