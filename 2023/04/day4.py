from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read().split("\n")

data = [cards.split(':')[1] for cards in data]

cards = [cards.split("|") for cards in data]

cards_list = [[stack[0].split(), stack[1].split()] for stack in cards]

common_cards = [list((Counter(stack[0]) & Counter(stack[1])).elements()) for stack in cards_list]

sum_common_cards = [2**max((len(i)-1), 0) for i in common_cards if len(i) != 0]

print(f"Answer 1: {sum(sum_common_cards)}")


# /*part 2*/

matched_before_update = []
matched_after_update = []
count_cards = []
pos = 1

for c in common_cards:
    cards_copies = list(range(pos+1, len(c)+pos+1))
    matched_before_update.append(cards_copies)
    matched_before_update = [item for row in matched_before_update for item in (row if isinstance(row, list) else [row])]
    count = matched_before_update.count(pos)
    count_cards.append(count+1)
    matched_before_update += cards_copies * count
    pos += 1

print(f"Answer 1: {sum(count_cards)}")

