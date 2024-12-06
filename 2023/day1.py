import re

lines = []

with open("day1_input.txt") as file:
    for line in file:
        lines.append(line.strip())

# lines.append("eighthree")

sum = 0

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
word_to_dig = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}

pattern = r'|'.join(map(re.escape, digits))
print(pattern)

for line in lines:
    # print(line)
    matches = list(re.findall(pattern, line))
    d1 = matches[0]
    matches = list(re.findall(pattern[::-1], line[::-1]))
    d2 = matches[0][::-1]
    print(line)
    print(f"{d1}, {d2}")
    if d1 in word_to_dig.keys():
        d1 = word_to_dig[d1]
    if d2 in word_to_dig.keys():
        d2 = word_to_dig[d2]
    print(f"{d1}, {d2}")
    a = int(d1+d2)
    print(a)
    sum += a

print(sum)

#53293 too low
#53395 too high