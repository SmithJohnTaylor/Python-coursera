import pandas as pd

fname = "flights.csv"

df = pd.read_csv(fname)
names = list()
for i, row in df.iterrows():
    if row["Name"] not in names:
        names.append(row["Name"])
names.sort()
print(names)