import re

eqns = []

with open("day7_input.txt") as file:
    for line in file:
        eqns.append(line.strip())

pattern = r'(\d+): (.*)'

count_1 = 0
a = 0
count_2 = 0

def possible(components, goal, current):
    if len(components)==0:
        return current==goal
    
    return (possible(components[1:], goal, current+components[0]) or 
            possible(components[1:], goal, current*components[0]))


def possible_1_2(components, goal):
    if len(components)==1:
        return (goal==components[0])
    
    if goal%components[-1]==0:
        return possible_1_2(components[:-1], goal/components[-1])
    else:
        return possible_1_2(components[:-1], goal-components[-1])

def possible_2(components, goal, current):
    if len(components)==0:
        return current==goal
    
    return (possible_2(components[1:], goal, current+components[0]) or 
            possible_2(components[1:], goal, current*components[0]) or
            possible_2(components[1:], goal, int(str(current) + str(components[0]))))

for eqn in eqns:
    match = re.findall(pattern, eqn)[0]

    num = int(match[0])
    components = [int(i) for i in match[1].split(" ")]

    # print(num)
    # print(components)

    if possible(components[1:], num, components[0]):
        count_1 += num

    if possible_1_2(components, num):
        a += num

    # if possible_2(components[1:], num, components[0]):
    #     count_2 += num

print("part 1")
print(count_1)
print(a)
# print("part 2")
# print(count_2)