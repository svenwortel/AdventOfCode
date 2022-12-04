import pandas as pd

df = pd.read_csv("input2.txt", header=None)

score = 0
for i in range(len(df)):
    game = df[0][i]
    if game == "A X":
        score += 4 # 1 + 3
    elif game == "A Y":
        score += 8 # 2 + 6
    elif game == "A Z":
        score += 3 # 3 + 0
    elif game == "B X":
        score += 1 # 1 + 0
    elif game == "B Y":
        score += 5 # 2 + 3
    elif game == "B Z":
        score += 9 # 3 + 6
    elif game == "C X":
        score += 7 # 1 + 6
    elif game == "C Y":
        score += 2 # 2 + 0
    elif game == "C Z":
        score += 6 # 3 + 3

print(score)

score = 0
for i in range(len(df)):
    game = df[0][i]
    if game == "A X":
        score += 3
    elif game == "A Y":
        score += 4
    elif game == "A Z":
        score += 8
    elif game == "B X":
        score += 1
    elif game == "B Y":
        score += 5
    elif game == "B Z":
        score += 9
    elif game == "C X":
        score += 2
    elif game == "C Y":
        score += 6
    elif game == "C Z":
        score += 7

print(score)