action = []
move = []

p1 = {"A": 1,
      "B": 2,
      "C": 3,
      }

p2 = {"X": 1,
      "Y": 2,
      "Z": 3,
      }

with open('input.txt', 'r') as f:
    f = f.read().split("\n")

for line in f:
    action.append(p2.get(line[2]))
    move.append(p1.get(line[0]))

i = 0
points = 0
while i < len(f):
    # lose
    if action[i] == 1 and move[i] > 1:
        points = points + 0 + move[i] - 1
    elif action[i] == 1 and move[i] == 1:
        points = points + 0 + move[i] + 2
    # draw
    elif action[i] == 2:
        points = points + 3 + move[i]
    # win
    elif action[i] == 3 and move[i] < 3:
        points = points + 6 + move[i] + 1
    else:
        points = points + 6 + move[i] - 2
    i += 1

print(points)
