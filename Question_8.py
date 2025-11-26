import pandas as pd

df = pd.read_csv("mtcars.csv")

cars_m_h = df[["mpg", "hp"]].copy()
cars_m_h_s = cars_m_h.iloc[9:35]

filtered = cars_m_h_s[(cars_m_h_s["mpg"] > 20) & (cars_m_h_s["hp"] > 100)]

print(filtered)
