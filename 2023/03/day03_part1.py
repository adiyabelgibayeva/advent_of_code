import pandas as pd

with open('input.txt', 'r') as f:
    data = f.read().split("\n")


data_list = [list(x) for x in data]

df = pd.DataFrame(data_list)

df.replace(".", None, inplace=True)
df.replace(to_replace=r'[^0-9]', value='*', regex=True, inplace=True)

numbers = []
current = []
save_current = False

for row in range(0, len(df)):
    for col in range(0, len(df.columns)):
        if df.loc[row, col] is not None and df.loc[row, col].isnumeric():
            current.append(df.loc[row, col])

            if save_current:
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
                    save_current = True

        else:
            if save_current:
                numbers.append(''.join(current))
                save_current = False
            current = []

    if save_current:
        numbers.append(''.join(current))
        save_current = False
    current = []

print(sum([int(x) for x in numbers]))
