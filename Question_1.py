import pandas as pd
import re

with open("sales.txt", "r") as f:
    lines = f.readlines()

clean_values = []

for line in lines:
    line = line.strip()

    if line == "" or line.lower() == "sales":
        continue

    line = line.replace("£", "").replace("$", "").replace(",", ".")
    
    value = re.findall(r"[\d.]+", line)
    if value:
        clean_values.append(float(value[0]))

usd_values = [round(v * 1.25, 2) for v in clean_values]

df = pd.DataFrame({"GBP": clean_values, "USD": usd_values})

df.to_csv("sales_cleaned.csv", index=False)

print("Cleaned currency data saved to sales_cleaned.csv")
print(df)
