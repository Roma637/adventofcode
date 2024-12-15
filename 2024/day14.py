import re 

width = 101
height = 103

# width = 11
# height = 7

def mapprint(width, height, bots):
    map = [[0 for j in range(width)] for i in range(height)]

    for bot in bots:
        map[bot[1]][bot[0]] += 1

    for i in map:
        print(''.join([str(j) if j!=0 else '.' for j in i ]))

def mapget(width, height, bots):    
    map = [[0 for j in range(width)] for i in range(height)]
    a = []

    for bot in bots:
        map[bot[1]][bot[0]] += 1

    for i in map:
        a.append(''.join([str(j) if j!=0 else '.' for j in i ]))

    return a

def safety_factor(width, height, bots):
    map = [[0 for j in range(width)] for i in range(height)]

    for bot in bots:
        map[bot[1]][bot[0]] += 1

    w_mid = width//2
    h_mid = height//2

    a = sum([sum(i[:w_mid]) for i in map[:h_mid]])
    b = sum([sum(i[w_mid+1:]) for i in map[:h_mid]])
    c = sum([sum(i[:w_mid]) for i in map[h_mid+1:]])
    d = sum([sum(i[w_mid+1:]) for i in map[h_mid+1:]])

    # print(a)
    # print(b)
    # print(c)
    # print(d)

    return (a*b*c*d)

pattern = r'p=(\d+),(\d+) v=([-0-9]+),([-0-9]+)'

with open("day14_input.txt") as file:
    bots = re.findall(pattern, file.read())

# with open("day14_eg_input.txt") as file:
#     bots = re.findall(pattern, file.read())

bots = [[int(j) for j in i] for i in bots]

time = 100
time = 103*101

b = []

for second in range(time):
    
    for bot in bots:
        bot[0], bot[1] = (bot[0]+bot[2])%width, (bot[1]+bot[3])%height

    m = mapget(width, height, bots)
    # print(m)
    for row in m:
        if '111111111111111' in row:
            # mapprint(width, height, bots)
            for line in m:
                print(line)
            print("--")
            print(second+1)
            print(safety_factor(width, height, bots))
            break

    b.append(safety_factor(width, height, bots))

print(min(b))

# print(bots)
# mapprint(width, height, bots)

# print("part 1")
# safety_factor(width, height, bots)

# xmas_tree = [[0 for j in range(width//2 - i)]+ (2*i + 1)*[1]+[0 for j in range(width//2 - i)] for i in range(height)]

# for line in xmas_tree:
#     print(line)