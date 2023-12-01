import regex as re

# /* part 1 */
with open('input.txt', 'r') as f:
    data = f.read().split("\n")

numbers = [re.findall("\d", str) for str in data]

print(f"Answer 1: {sum([int(i[0]+i[-1]) for i in numbers])}")

# /* part 2 */
dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9}
data_new = []

numbers = [re.findall("\d|one|two|three|four|five|six|seven|eight|nine", str, overlapped=True) for str in data]

numbers = ["".join(i) for i in numbers]

numbers_new = []
for i in numbers:
    for keys in dict.keys():
        if re.findall(keys, i):
            i = i.replace(keys, str(dict[keys]))
    numbers_new.append(i)

print(f"Answer 2: {sum([int(i[0]+i[-1]) for i in numbers_new])}")



