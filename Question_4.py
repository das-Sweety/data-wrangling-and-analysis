import pandas as pd

df = pd.read_csv("mtcars.csv")

cars_m_h = df[["mpg", "hp"]].copy()
cars_m_h.columns = ["miles_per_gallon", "horse_power"]

print(cars_m_h)
