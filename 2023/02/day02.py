import re

with open('input.txt', 'r') as f:
    games = f.read().split("\n")

games = [game.split(':')[1] for game in games]

i = 0
sum_game = 0
for game in games:
    i = i + 1
    max_red = 0
    max_green = 0
    max_blue = 0
    for j in re.findall("(\d+) (\w+)", game):
        value = int(j[0])
        if j[1] == "red" and value > max_red:
            max_red = value
        if j[1] == "green" and value > max_green:
            max_green = value
        if j[1] == "blue" and value > max_blue:
            max_blue = value
    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        sum_game = sum_game + i

print(f"Answer 1: {sum_game}")

#/* part 2 */
cube_value = 0
for game in games:
    i = i + 1
    max_red = 0
    max_green = 0
    max_blue = 0
    for j in re.findall("(\d+) (\w+)", game):
        value = int(j[0])
        if j[1] == "red" and value > max_red:
            max_red = value
        if j[1] == "green" and value > max_green:
            max_green = value
        if j[1] == "blue" and value > max_blue:
            max_blue = value
    cube_value = cube_value + max_blue * max_red * max_green

print(f"Answer 2: {cube_value}")



