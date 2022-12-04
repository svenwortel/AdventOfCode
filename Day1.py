import pandas as pd

df = pd.read_csv("input1.txt", header=None, skip_blank_lines=False)

df_list = []
for _, g in df.groupby(df.isnull().cumsum().values.ravel()):
    df_list.append(g.dropna().reset_index(drop=True))

df = pd.concat(df_list, axis=1, ignore_index=True)

calorie_sums = [df.loc[:, i].sum() for i in range(df.shape[1])]

print(max(calorie_sums))
print(sorted(calorie_sums)[-1] + sorted(calorie_sums)[-2] + sorted(calorie_sums)[-3])