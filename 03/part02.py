with open('input.txt', 'r') as f:
    f = f.read().split("\n")

i = 0
m = []
tmp = []

while i < len(f):
    tmp.append(f[i])
    i += 1
    if i % 3 == 0:
        m.append(tmp)
        tmp = []

total = 0

for l in m:
    a = {}
    for x in l[0]:
        a[x] = 1
    for x in l[1]:
        if a.get(x) == 1:
            a[x] = 2
    for x in l[2]:
        if a.get(x) == 2:
            num = ord(x)
            if x.islower():
                num -= 96
            else:
                num -= 38
            total += num
            break

print(total)


