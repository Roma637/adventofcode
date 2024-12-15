with open("day12_input.txt") as file:
    field = file.read().strip().split("\n")

def mapprint(map):
    for i in map:
        # print(''.join(i))
        print(i)

# field = ['AAAA',
# 'BBCD',
# 'BBCC',
# 'EEEC'
# ]

# field = ['OOOOO',
# 'OXOXO',
# 'OOOOO',
# 'OXOXO',
# 'OOOOO',
# ]

# field = ['RRRRIICCFF',
# 'RRRRIICCCF',
# 'VVRRRCCFFF',
# 'VVRCCCJFFF',
# 'VVVVCJJCFE',
# 'VVIVCCJJEE',
# 'VVIIICJJEE',
# 'MIIIIIJJEE',
# 'MIIISIJEEE',
# 'MMMISSJEEE'
# ]

mapprint(field)

# plants = []
# area = {}
# peri = {}
visited = [[False for j in range(len(field[0]))] for i in range(len(field))]

# for row in field:
#     for col in row:
#         if col not in plants:
#             plants.append(col)
            # area[col]=0
            # peri[col]=0

# print(plants)
# print(area)
# print(peri)
# print(visited)

# dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def get_area_helper(row, col, char):
    if (not(0 <= row < len(field)) or
        not(0 <= col < len(field[0])) or
        field[row][col]!=char or
        visited[row][col]):
        return 0
    
    print(f"area helper {row},{col}")
    visited[row][col] = True

    return (1 + get_area_helper(row+1, col, char) + 
                get_area_helper(row, col+1, char) + 
                get_area_helper(row-1, col, char) + 
                get_area_helper(row, col-1, char))

def get_area(row, col):
    char = field[row][col]
    visited[row][col] = True

    return (1 + get_area_helper(row+1, col, char) + 
                get_area_helper(row, col+1, char) + 
                get_area_helper(row-1, col, char) + 
                get_area_helper(row, col-1, char))

# print(field[0][0])
# print(get_area(0,0))

def get_peri_helper(row, col, char):
    if (not(0 <= row < len(field)) or
        not(0 <= col < len(field[0])) or
        field[row][col]!=char or
        visited[row][col]):
        return 0
    
    visited[row][col] = True

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    count = 0

    for i in range(4):
        if (not(0 <= row+dirs[i][0] < len(field)) or
            not(0 <= col+dirs[i][1] < len(field[0])) or
            field[row+dirs[i][0]][col+dirs[i][1]]!=char):
            count += 1

    return (count + get_peri_helper(row+1, col, char) +
                get_peri_helper(row, col+1, char) +
                get_peri_helper(row-1, col, char) +
                get_peri_helper(row, col-1, char))

def get_peri(row, col):
    char = field[row][col]
    visited[row][col] = True

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    count = 0

    for i in range(4):
        if (not(0 <= row+dirs[i][0] < len(field)) or
            not(0 <= col+dirs[i][1] < len(field[0])) or
            field[row+dirs[i][0]][col+dirs[i][1]]!=char):
            count += 1

    return (count + get_peri_helper(row+1, col, char) +
                    get_peri_helper(row, col+1, char) +
                    get_peri_helper(row-1, col, char) +
                    get_peri_helper(row, col-1, char))

# print(field[0][0])
# print(get_peri(1,0))

def probe(row, col, char):

    if (not(0 <= row < len(field)) or
        not(0 <= col < len(field[0])) or
        field[row][col]!=char):
        return 0,1
    
    if (visited[row][col]):
        return 0,0

    visited[row][col] = True

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    a = 1
    p = 0

    # if a direction has a match then it's +1 to area and probe that
    # otherwise it's +1 to perimeter and stop!

    for i in range(4):
        aa, pp = probe(row+dirs[i][0], col+dirs[i][1], char)
        a += aa
        p += pp

    return a,p

# print(probe(1, 2, field[1][2]))

def probe_2(row, col, char):
    if (not(0 <= row < len(field)) or
        not(0 <= col < len(field[0])) or
        field[row][col]!=char):
        #here we need to start traveling the edges
        #like probe along?
        pass
    
    if (visited[row][col]):
        return 0,0
    
    visited[row][col] = True

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    a = 1
    p = 0

    # if a direction has a match then it's +1 to area and probe that
    # otherwise it's +1 to perimeter and stop!

    for i in range(4):
        aa, pp = probe(row+dirs[i][0], col+dirs[i][1], char)
        a += aa
        p += pp

    return a,p

count_1 = 0

for row in range(len(field)):
    for col in range(len(field[0])):
        if not(visited[row][col]):
            char = field[row][col]
            print(char)
            a, p = probe(row, col, char)
            print(f"{a} * {p} = {a*p}")
            count_1 += a*p

print(count_1)