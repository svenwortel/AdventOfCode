import pandas as pd
import numpy as np

columns = ['0', '1', '3']
data4 = pd.read_csv("input4.txt", header=None, sep="-", names=columns)
data4[["1", "2"]] = data4["1"].str.split(",", expand=True)

data4 = data4.reindex(columns=['0', '1', '2', '3'])


def contains(lower1, upper1, lower2, upper2):
    if lower1 <= lower2 and upper1 >= upper2:
        return True
    elif lower2 <= lower1 and upper2 >= upper1:
        return True

count = 0
for i in range(data4.shape[0]):
    if contains(int(data4.iloc[i][0]), int(data4.iloc[i][1]), int(data4.iloc[i][2]), int(data4.iloc[i][3])):
       count += 1

print(count)


def overlaps(lower1, upper1, lower2, upper2):
    if lower1 <= lower2 and upper1 >= lower2:
        return True
    elif lower1 <= upper2 and upper1 >= upper2:
        return True
    elif lower2 <= lower1 and upper2 >= lower1:
        return True
    elif lower2 <= upper1 and upper2 >= upper1:
        return True

overlap_count = 0
for i in range(data4.shape[0]):
    if overlaps(int(data4.iloc[i][0]), int(data4.iloc[i][1]), int(data4.iloc[i][2]), int(data4.iloc[i][3])):
        overlap_count += 1

print(overlap_count)