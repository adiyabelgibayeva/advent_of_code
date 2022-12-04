d = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

with open('input.txt', 'r') as f:
    f = f.read().split("\n")

data = []
for line in f:
    data.append(d.get(line))

print(sum(data))