import numpy as np
import pandas as pd

data3 = pd.read_csv("input3.txt", header=None)
typestotal = []

for i in range(data3.shape[0]):
    types = []
    backpack = data3[0][i]
    item_count = len(backpack)
    compartment1 = backpack[:int(item_count/2)]
    compartment2 = backpack[int(item_count/2):]
    for j in range(len(compartment1)):
        for k in range(len(compartment2)):
            if compartment1[j] == compartment2[k]:
                if compartment1[j] not in types:
                    types.append(compartment1[j])
    typestotal += types

unique_types = list(set(unique_types))

def alphabet_position2(text):
    d = {L: int(i) for i, L in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}

    result = 0
    for t in text:
        result += d.get(t, t)

    return result

print(alphabet_position2(typestotal))


priority = ""

for i in range(0,data3.shape[0],3):
    df = data3.iloc[i:i+3]
    elf1 = sorted(list(set(df[0][i])))
    elf2 = sorted(list(set(df[0][i + 1])))
    elf3 = sorted(list(set(df[0][i + 2])))
    for item in elf1:
        if item in elf2 and item in elf3:
            priority += item


print(alphabet_position2(priority))