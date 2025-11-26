import pandas as pd

df = pd.read_csv("mtcars.csv")

cars_m_h = df[["mpg", "hp"]].copy()
cars_m_h_s = cars_m_h.iloc[9:35]  

print(cars_m_h_s)
