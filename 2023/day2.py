import re

games = []

pattern = r'Game (\d+): (.*)\n'

count = 0
powers = 0

with open("day2_input.txt") as file:
    for line in file:

        matches = re.findall(pattern, line)
        match = matches[0]

        game_id = int(match[0])
        details = [i.strip().split(", ") for i in match[1].split(";")]

        # print(game_id)
        # print(details)

        numbers = {'red':0, 'green':0, 'blue':0}

        for round in details:
            for col in round:
                a = col.split(" ")
                a[0] = int(a[0])
                if (a[0]) > numbers[a[1]]:
                    numbers[a[1]] = a[0]

        # do the comparison and += 

        # print(numbers)

        if (numbers['red']<=12 and 
            numbers['green']<=13 and
            numbers['blue']<=14):
            count += game_id

        powers += numbers['red'] * numbers['green'] * numbers['blue']

print("part 1")
print(count)
print("part 2")
print(powers)