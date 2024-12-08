with open("day8_input.txt") as file:
    map = [list(i) for i in file.read().strip().split("\n")]

# map = [
# '............',
# '........0...',
# '.....0......',
# '.......0....',
# '....0.......',
# '......A.....',
# '............',
# '............',
# '........A...',
# '.........A..',
# '............',
# '............'
# ]

# map = [list(i) for i in map]

def mapprint(map):
    print('--')
    for i in map:
        print(''.join(i))
    print('--')

mapprint(map)

# print(map)

coords = {}

for row in range(len(map)):
    for col in range(len(map[row])):
        char = map[row][col]
        if char=='.':
            continue
        if char in coords:
            coords[char].append((row,col))
        else:
            coords[char] = [(row,col)]

print(coords)

for key in coords:
    # find antinodes for every possible pair
    for i in range(len(coords[key])):
        row_a,col_a=coords[key][i]
        for j in range(i+1, len(coords[key])):
            #i and j are tuples of row,col
            row_b,col_b=coords[key][j]

            row_diff = row_a-row_b
            col_diff = col_a-col_b

            #a+diffs

            if (0 <= row_a + row_diff < len(map)) and (0 <= col_a + col_diff < len(map[row_a + row_diff])):
                map[row_a + row_diff][col_a + col_diff] = '#'

            #b-diffs

            if (0 <= row_b - row_diff < len(map)) and (0 <= col_b - col_diff < len(map[row_b - row_diff])):
                map[row_b - row_diff][col_b - col_diff] = '#'

count_1 = 0

for row in map:
    count_1 += row.count('#')

# print("part 1")
# print(count_1)

# mapprint(map)

for key in coords:
    # find antinodes for every possible pair
    for i in range(len(coords[key])):
        for j in range(i+1, len(coords[key])):
            #i and j are tuples of row,col
            row_a,col_a=coords[key][i]
            row_b,col_b=coords[key][j]

            row_diff = row_a-row_b
            col_diff = col_a-col_b

            #a+diffs

            while (0 <= row_a < len(map)) and (0 <= col_a < len(map[row_a])):
                map[row_a][col_a] = '#'
                row_a += row_diff
                col_a += col_diff

            #b-diffs

            while (0 <= row_b < len(map)) and (0 <= col_b < len(map[row_b])):
                map[row_b][col_b] = '#'
                row_b -= row_diff
                col_b -= col_diff

# ideal = ['##....#....#',
# '.#.#....0...',
# '..#.#0....#.',
# '..##...0....',
# '....0....#..',
# '.#...#A....#',
# '...#..#.....',
# '#....#.#....',
# '..#.....A...',
# '....#....A..',
# '.#........#.',
# '...#......##']
# ideal = [list(i) for i in ideal]

mapprint(map)
# mapprint(ideal)

count_2 = 0 

for row in map:
    count_2 += row.count('#')

print("part 2")
print(count_2)

# # put the letters back

# for key in coords:
#     for row,col in coords[key]:
#         map[row][col] = key

# # put the dots back

# for row in range(len(map)):
#     for col in range(len(map[row])):
#         if map[row][col]=='#':
#             map[row][col]='.'

# mapprint(map)