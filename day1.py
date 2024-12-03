list1 = []
list2 = []

with open('day1_input.txt') as file:
    for line in file:
        list1.append(int(line.split("   ")[0]))
        list2.append(int(line.split("   ")[1].strip()))

# print(list1)
# print(list2)

list1.sort()
list2.sort()

print("part 1")
print(sum([abs(list1[i] - list2[i])for i in range(len(list1))]))
print("part 2")
print(sum([(list1[i] * list2.count(list1[i])) for i in range(len(list1))]))