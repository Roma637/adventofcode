import re

rules = []

with open("day5_1_input.txt") as file:
    pattern = r'(\d*)\|(\d*)'
    for line in file:
        m = re.match(pattern, line.strip())
        rules.append((int(m.group(1)), int(m.group(2))))

# print(rules)

after = {}
before = {}

for bef,aft in rules:
    if bef in after:
        after[bef].append(aft)
    else:
        after[bef] = [aft]

    if aft in before:
        before[aft].append(bef)
    else:
        before[aft] = [bef]

# print(after)
# print(before)

updates = []

with open("day5_2_input.txt") as file:
    for line in file:
        updates.append(eval("[" + line.strip() + "]"))

# print(updates)

def valid(update):
    for i in range(len(update)):
        a = update[i]
        for j in range(i+1, len(update)):
            b = update[j]

            if (b in before[a] or a in after[b]):
                return False
            
    else:
        return True 


count_1 = 0
count_2 = 0

for update in updates:
    if valid(update):
        mid = len(update)//2
        count_1 += update[mid]
    else:
        # re order update somehow
        new = []

        for elem in update:
            i = 0
            while (i < len(new)) and (new[i] in before[elem]):
                i += 1
            new.insert(i, elem)

        #then add
        mid = len(new)//2
        count_2 += new[mid]

print("part 1")
print(count_1)
print("part 2")
print(count_2)
