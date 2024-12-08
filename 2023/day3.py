schem  = []

with open("day3_input.txt") as file:
    for line in file:
        schem.append(line.strip())

# schem = ['467..114..',
# '...*......',
# '..35..633.',
# '......#...',
# '617*......',
# '.....+.58.',
# '..592.....',
# '......755.',
# '...$.*....',
# '.664.598..']

dir = [-1, 0, 1]

count_1 = 0
count_2 = 0

def mapprint(map):
    print('--')
    for i in map:
        print(''.join(i))
    print('--')

# PLEASE COMMENT OUT PART 1 IF DOING PART 2
for y in range(len(schem)):
    for x in range(len(schem[y])):
        #part 1
        if schem[y][x]!='.' and not(schem[y][x].isnumeric()):
            # mapprint(schem)
            # must check all 8 directions

            for q in range(3):
                a = dir[q]
                for w in range(3):
                    b = dir[w]

                    if (0<=y+a<len(schem)) and (0<=x+b<len(schem[y+a])):
                        ch = schem[y+a][x+b]
                        # print(ch)
                        if ch.isnumeric():
                            i = x+b
                            while (0<i and schem[y+a][i-1].isnumeric()):
                                i -= 1
                            j = x+b
                            while (j<len(schem[y+a]) and schem[y+a][j].isnumeric()):
                                j += 1
                            
                            count_1 += int(schem[y+a][i:j])
                            schem[y+a] = schem[y+a][:i] + (j-i)*'.' + schem[y+a][j:]

        #part 2
        if schem[y][x]=='*':
            nums = []

            for q in range(3):
                a = dir[q]
                for w in range(3):
                    b = dir[w]

                    if (0<=y+a<len(schem)) and (0<=x+b<len(schem[y+a])):
                        ch = schem[y+a][x+b]

                        if ch.isnumeric():
                            i = x+b

                            while (0<i and schem[y+a][i-1].isnumeric()):
                                i -= 1

                            j = x+b

                            while (j<len(schem[y+a]) and schem[y+a][j].isnumeric()):
                                j += 1

                            nums.append(int(schem[y+a][i:j]))
                            schem[y+a] = schem[y+a][:i] + (j-i)*'.' + schem[y+a][j:]
            
            if len(nums)==2:
                count_2 += nums[0]*nums[1]



print("part 1")
print(count_1)
print("part 2")
print(count_2)