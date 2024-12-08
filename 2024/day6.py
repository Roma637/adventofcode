map = []

with open("day6_input.txt") as file:
    for line in file:
        map.append(list(line.strip()))

# map = ['....#.....',
# '.........#',
# '..........',
# '..#.......',
# '.......#..',
# '..........',
# '.#..^.....',
# '........#.',
# '#.........',
# '......#...']

# map = ['...#',
# '#...',
# '.^..',
# '.#..']

map = [list(i) for i in map]

def mapprint(map):
    for i in map:
        print(''.join(i))

# mapprint(map)

x = -1
y = -1

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j]=='^':
            x = j
            y = i
    #         break
    # if x!=-1:
    #     break

init_x = x
init_y = y

dir = {'x':0, 'y':-1}

while (0<=y<len(map)) and (0<=x<len(map[0])):
    while ((0<=y+dir['y']<len(map)) and 
           (0<=x+dir['x']<len(map[0]) and 
            map[y+dir['y']][x+dir['x']] != '#')):
        
        map[y][x]='X'
        y += dir['y']
        x += dir['x']

    if not((0<=y+dir['y']<len(map)) and (0<=x+dir['x']<len(map[0]))):
        map[y][x]='X'
        break

    # turn 90 degrees
    dir['y'], dir['x'] = dir['x'], -1*dir['y']

    # map[y][x]='X'
    # y += dir['y']
    # x += dir['x']


# mapprint(map)

count = 0

for row in map:
    count += row.count('X')

print("part 1")
print(count)

# we know that guard is stuck in loop when: x,y match initial positions WHILE dir is 0,-1

potential = []

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j]=='X':
            potential.append((i,j))
            map[i][j] = '.'

map[init_y][init_x] = '^'

# map = []

# with open("day6_input.txt") as file:
#     for line in file:
#         map.append(list(line.strip()))

# init_x = -1
# init_y = -1

# for i in range(len(map)):
#     for j in range(len(map[i])):
#         if map[i][j]=='^':
#             init_x = j
#             init_y = i

dir = {'x':0, 'y':-1}

def will_cause_loop(i,j):

    # print(f"now checking for {i} {j}")

    x = init_x
    y = init_y

    dir = {'x':0, 'y':-1}

    map[i][j]='#'
    # mapprint(map)

    visited = []
    to_app = [y, x, dir.copy()]
    visited.append(to_app)
    # print(f"visited initially is {visited}")

    while (0<=y<len(map)) and (0<=x<len(map[0])):
        while ((0<=y+dir['y']<len(map)) and (0<=x+dir['x']<len(map[0]) and map[y+dir['y']][x+dir['x']] != '#')):
            
            # map[y][x]='X'
            y += dir['y']
            x += dir['x']

            # print(f"{y} {x}")

        if not((0<=y+dir['y']<len(map)) and (0<=x+dir['x']<len(map[0]))):
            break
        
        # turn 90 degrees
        dir['y'], dir['x'] = dir['x'], -1*dir['y']
        # print("TURNING")

        to_app = [y,x, dir.copy()]
        # print(f"to_app is {to_app}")

        # if (to_app in visited):
        #     print(visited[0]==to_app)
        #     map[i][j]='.'
        #     print(f"found previously visited {to_app}")
        #     return True
        
        for visit in visited:
            # print(f"visit is {visit}")
            if (visit[0]==to_app[0] and 
                visit[1]==to_app[1] and 
                visit[2]['x']==to_app[2]['x'] and 
                visit[2]['y']==to_app[2]['y']):

                # print(f"{visit[2]['x']}=={to_app[2]['x']}")
                # print(f"{visit[2]['y']}=={to_app[2]['y']}")
                map[i][j]='.'
                # print(f"found previously visited {to_app}")
                return True
        
        visited.append(to_app)
        # print(visited)

    map[i][j]='.'
    return False

count = 0 

# mapprint(map)

for i,j in potential:
    if will_cause_loop(i,j):
        count += 1

print("part 2")
print(count)