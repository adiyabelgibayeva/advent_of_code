with open('input.txt', 'r') as f:
    f = f.read().split("\n")

rucksack = []
for line in f:
    length = int(len(line) / 2)
    rucksack.append([line[:length], line[length:]])


letter = []
total = 0
for item in rucksack:
    a = {}
    for x in item[0]:
        a[x] = True
    for y in item[1]:
        if a.get(y):
            num = ord(y)
            if y.islower():
                num -= 96
            else:
                num -= 38
            total += num
            break

print(total)
