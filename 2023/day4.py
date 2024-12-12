counts = [0]
cards = [([0],[0])]

with open("day4_input.txt") as file:
    # cards = file.read().strip().split("\n")

    for line in file:
        numbas = line.strip().split(": ")[1].split(" | ")
        winning = [int(i.strip()) for i in numbas[0].split(" ") if i!='']
        yours = [int(i.strip()) for i in numbas[1].split(" ") if i!='']
        cards.append((winning,yours))
        counts.append(1)

# file = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
# 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
# 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
# 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
# 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
# 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
# ]

# for line in file:
#     numbas = line.strip().split(": ")[1].split(" | ")
#     winning = [int(i.strip()) for i in numbas[0].split(" ") if i!='']
#     yours = [int(i.strip()) for i in numbas[1].split(" ") if i!='']
#     cards.append((winning,yours))
#     counts.append(1)

# print(cards)
# print(counts)

count_1 = 0

for i in range(1,len(cards)):
    winning,yours = cards[i]
    matches = 0
    for num in winning:
        if num in yours:
            matches += 1
    if matches>0:
        points = 2**(matches-1)
        count_1 += points
        for j in range(matches):
            counts[i+j+1] += counts[i]

print("part 1")
print(count_1)
print("part 2")
print(sum(counts))