with open('input.txt', 'r') as f:
    f = [[x for x in line.split(",")] for line in f.read().split("\n")]

data = []
q1 = 0
q2 = 0
for x in f:
    a = int(x[0].split('-')[0])
    b = int(x[0].split('-')[1])
    c = int(x[1].split('-')[0])
    d = int(x[1].split('-')[1])
    if (a <= c and b >= d) or (c <= a and d >= b):
        q1 += 1
    if (a <= d and b >= c) or (a <= d <= b):
        q2 += 1

print(q1)
print(q2)
