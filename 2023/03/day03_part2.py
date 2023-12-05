import pandas as pd
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().split("\n")

data_list = [list(x) for x in data]

df = pd.DataFrame(data_list)

df.replace(".", None, inplace=True)

world = {}
current_number = []
save_current_number = False
current_pos = (0, 0)

for row in range(0, len(df)):
    for col in range(0, len(df.columns)):
        if df.loc[row, col] is not None and df.loc[row, col].isnumeric():
            current_number.append(df.loc[row, col])

            if save_current_number:
                continue

            bounds_around = [
                [0, 1],
                [0, -1],
                [-1, 0],
                [-1, 1],
                [-1, -1],
                [1, 0],
                [1, 1],
                [1, -1]
            ]

            for b in bounds_around:
                x = b[0] + row
                y = b[1] + col

                if 0 < x < len(df) and 0 < y < len(df.columns) and df.loc[x, y] == "*":
                    save_current_number = True
                    current_pos = (x, y)
        else:
            if save_current_number:
                digit = world.get(current_pos, [])
                digit.append(''.join(current_number))
                world[current_pos] = digit
                save_current_number = False
            current_number = []

    if save_current_number:
        digit = world.get(current_pos, [])
        digit.append(''.join(current_number))
        world[current_pos] = digit
        save_current_number = False
    current_number = []


sum = 0

for k, v in world.items():
    if len(v) == 2:
        sum += int(v[0]) * int(v[1])

print(sum)
