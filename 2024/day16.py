with open("day16_input.txt") as file:
    maze = [list(i) for i in file.read().split("\n")]

def mapprint():
    for i in maze:
        print(''.join(i))

# maze = [
#     '###############',
# '#.......#....E#',
# '#.#.###.#.###.#',
# '#.....#.#...#.#',
# '#.###.#####.#.#',
# '#.#.#.......#.#',
# '#.#.#####.###.#',
# '#...........#.#',
# '###.#.#####.#.#',
# '#...#.....#.#.#',
# '#.#.#.###.#.#.#',
# '#.....#...#.#.#',
# '#.###.#.#.#.#.#',
# '#S..#.....#...#',
# '###############'
# ]

# maze = [
#     '#################',
# '#...#...#...#..E#',
# '#.#.#.#.#.#.#.#.#',
# '#.#.#.#...#...#.#',
# '#.#.#.#.###.#.#.#',
# '#...#.#.#.....#.#',
# '#.#.#.#.#.#####.#',
# '#.#...#.#.#.....#',
# '#.#.#####.#.###.#',
# '#.#.#.......#...#',
# '#.#.###.#####.###',
# '#.#.#...#.....#.#',
# '#.#.#.#####.###.#',
# '#.#.#.........#.#',
# '#.#.#.#########.#',
# '#S#.............#',
# '#################'
# ]

maze = [list(i) for i in maze]

print(maze)

# mapprint(maze)

# dirs = [(0,1),(1,0),(0,-1),(-1,0)]
# curr_dir = (0,1)

#row,col

start = [139,1]
end = [1,139]
maze[139][1]='.'

# start = [13,1]
# end = [1,13]
# maze[13][1]='.'

# start = [15,1]
# end = [1,15]
# maze[15][1]='.'

paths = []

def probe(current, moveset):

    # print(f"{current}")

    if (maze[current[0]][current[1]]=='E'):
        global paths
        print("=====FOUND THE END====")
        paths.append(moveset)

    elif (not(0 < current[0] < len(maze)-1) or
        not(0 < current[1] < len(maze[0])-1) or
        (maze[current[0]][current[1]]!='.')):
        return
    
    else:

        # mapprint()

        print(moveset)

        maze[current[0]][current[1]]='^'
        probe([current[0]-1,current[1]], moveset+'^')

        maze[current[0]][current[1]]='v'
        probe([current[0]+1,current[1]], moveset+'v')

        maze[current[0]][current[1]]='>'
        probe([current[0],current[1]+1], moveset+'>')

        maze[current[0]][current[1]]='<'
        probe([current[0],current[1]-1], moveset+'<')

        maze[current[0]][current[1]]='.'
        
probe(start, '')

print(paths)