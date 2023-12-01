with open('input.txt', 'r') as f:
    data = [[int(x) for x in line.split("\n")] for line in f.read().split("\n\n")]

total = []

for elfs in data:
    total.append(sum(elfs))

print(max(total))

total.sort(reverse=True)
print(sum(total[:3]))
