import pandas as pd

df = pd.read_csv("mtcars.csv")

cars_m_h = df[["mpg", "hp"]].copy()
cars_m_h_s = cars_m_h.iloc[9:35]

cars_m_h_s_no_dup = cars_m_h_s.drop_duplicates()

print(cars_m_h_s_no_dup)
