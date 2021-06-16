import pandas as pd
import csv

df = pd.read_csv("brown_dwarfs.csv")
df = df[df["no"].notna()]
df = df[df["Star_name"].notna()]
df = df[df["Distance"].notna()]
df = df[df["Mass"].notna()]
df = df[df["Radius"].notna()]
df["Radius"] *= 0.102763
df["Mass"] = (
    df["Mass"].apply(lambda x: x.replace("$", "").replace(",", "")).astype("float")
)
df["Mass"] *= 0.000954588
df.to_csv("brown_dwarfs.csv")
ds1 = []
ds2 = []
with open("brown_dwarfs.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        ds1.append(row)
with open("brightest_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        ds2.append(row)
h1 = ds1[0]
h2 = ds2[0]
headers = h1 + h2
pd1 = ds1[1:]
pd2 = ds2[1:]

pld = []
# for index, row in enumerate(pd1):
#     pld.append(pd1[index] + pd2[index])
for i in pd1:
    pld.append(i)
for ii in pd2:
    pld.append(ii)

with open("combinded_data.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(pld)
