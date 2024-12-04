from re import findall

str = ''

with open("day3_input.txt") as file:
    for line in file:
        str += line

commands = findall(r'mul\([0-9]+,[0-9]+\)', str)
# print(commands)

def mul(a,b):
    return a*b

sum = 0

for exp in commands:
    sum += eval(exp)

print("part 1")
print(sum)

commands_mod = findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", str)
# print(commands_mod)

flag = True
sum = 0 

for exp in commands_mod:
    if exp=="do()":
        flag = True
    elif exp=="don't()":
        flag = False
    elif flag:
        sum += eval(exp)

print("part 2")
print(sum)