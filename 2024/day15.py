def mapprint(map):
    for i in map:
        print(''.join(i))
    print("--")

warehouse = []

with open("day15_1_input.txt") as file:
    for line in file:
        warehouse.append(list(line.strip()))

# warehouse = [
#     '########',
# '#..O.O.#',
# '##@.O..#',
# '#...O..#',
# '#.#.O..#',
# '#...O..#',
# '#......#',
# '########',
# ]

# warehouse = [
#     '##########',
# '#..O..O.O#',
# '#......O.#',
# '#.OO..O.O#',
# '#..O@..O.#',
# '#O#..O...#',
# '#O..O..O.#',
# '#.OO.O.OO#',
# '#....O...#',
# '##########',
# ]

warehouse = [list(i) for i in warehouse]

moves = []

with open("day15_2_input.txt") as file:
    for line in file:
        moves.extend(list(line.strip()))

# moves = [i for i in '<^^>>>vv<v>>v<<']
# moves = [i for i in '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^']

# ideal = [
#     '########',
# '#....OO#',
# '##.....#',
# '#.....O#',
# '#.#O@..#',
# '#...O..#',
# '#...O..#',
# '########',
# ]

# ideal = ['##########',
# '#.O.O.OOO#',
# '#........#',
# '#OO......#',
# '#OO@.....#',
# '#O#.....O#',
# '#O.....OO#',
# '#O.....OO#',
# '#OO....OO#',
# '##########'
# ]

moveset = {'<':{'row':0,'col':-1}, 
           '>':{'row':0,'col':1}, 
           'v':{'row':1,'col':0}, 
           '^':{'row':-1,'col':0}}

mapprint(warehouse)
print(moves)

for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j]=='@':
            robot_pos = {'row':i, 'col':j}

print(robot_pos)

def box_move(box_row, box_col, space_row, space_col, can_do):
    if (not(0 <= space_row < len(warehouse)) or 
        not(0 <= space_col < len(warehouse[0])) or
        warehouse[space_row][space_col]=='#'):
        can_do = False
    elif (warehouse[space_row][space_col]=='O'):
        diff_row = space_row - box_row
        diff_col = space_col - box_col

        print(f"recursive call, now trying to push {space_row},{space_col} to {space_row+diff_row},{space_col+diff_col}")
        can_do = box_move(space_row, space_col, space_row+diff_row, space_col+diff_col, can_do)

    print(f"can_do is {can_do}")

    if can_do:
        warehouse[space_row][space_col] = 'O'
        warehouse[box_row][box_col] = '.'
        return True
    else:
        return False


def robot_move(move):
    global robot_pos
    goal_row = robot_pos['row'] + moveset[move]['row']
    goal_col = robot_pos['col'] + moveset[move]['col']

    can_do = True

    if warehouse[goal_row][goal_col]=='#':
        return 
    elif warehouse[goal_row][goal_col]=='O':
        print("BOX")
        diff_row = goal_row - robot_pos['row']
        diff_col = goal_col - robot_pos['col']
        print(f"box is at {goal_row},{goal_col}")
        print(f"box should go {goal_row+diff_row},{goal_col+diff_col}")
        can_do = box_move(goal_row, goal_col, goal_row+diff_row, goal_col+diff_col, True)

    if can_do:
        warehouse[goal_row][goal_col]='@'
        warehouse[robot_pos['row']][robot_pos['col']]='.'
        robot_pos = {'row':goal_row, 'col':goal_col}

    
for move in moves:
    robot_move(move)
    print(f"move is {move}")
    # mapprint(warehouse)
    print(robot_pos)

mapprint(warehouse)
# mapprint(ideal)

count_1 = 0

for row in range(len(warehouse)):
    for col in range(len(warehouse[0])):
        if warehouse[row][col]=='O':
            # print(f"{row},{col}")
            # print(f"{100*row + col}")
            count_1 += 100*row + col
            # print(count_1)
            # print("--")

print(count_1)