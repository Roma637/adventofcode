with open("day10_input.txt") as file:
    mtn = file.read().split("\n")

# mtn = ['89010123',
# '78121874',
# '87430965',
# '96549874',
# '45678903',
# '32019012',
# '01329801',
# '10456732']

# mtn = ['0123',
# '1234',
# '8765',
# '9876']

# mtn = ['9990999',
# '9991999',
# '9992999',
# '6543456',
# '7999997',
# '8111118',
# '9111119']

# visited = [[False for i in range(len(mtn[0]))] for j in range(len(mtn))]
# print(visited)

def mtnprint(mtn):
    for i in mtn:
        print(''.join(i))

# mtnprint(mtn)

# def score_helper(row, col, prevrow, prevcol):
#     if (not(0 <= row < len(mtn)) or 
#         not(0 <= col < len(mtn[row])) or
#         int(mtn[row][col]) - int(mtn[prevrow][prevcol]) != 1):
#         return 0

#     if mtn[row][col]=='9':
#         return 1
    
#     return (score_helper(row+1, col+1, row, col) + 
#             score_helper(row-1, col+1, row, col) +
#             score_helper(row+1, col-1, row, col) +
#             score_helper(row-1, col-1, row, col))
    
# def score(row, col):
#     return (score_helper(row+1, col+1, row, col) + 
#             score_helper(row-1, col+1, row, col) +
#             score_helper(row+1, col-1, row, col) +
#             score_helper(row-1, col-1, row, col))

def score(row, col):

    # visited[row][col] = True
    # print(visited)

    # print(f"{row}, {col} - number is {mtn[row][col]}")

    if mtn[row][col]=='9':
        return 1

    s = 0

    dirs = [(1,0), (0,1), (0,-1), (-1,0)]

    for dir in dirs:
        a = row+dir[0]
        b = col+dir[1]

        # print(f"a and b are {a},{b}")

        if ( (0 <= a < len(mtn))and
             (0 <= b < len(mtn[a]))and
            #  not visited[a][b] and 
            (int(mtn[a][b]) - int(mtn[row][col]) == 1)):
            s += score(a, b)

    return s

# def rating(row, col):
#     # number of unique 

score_sum = 0

for row in range(len(mtn)):
    for col in range(len(mtn[row])):
        if mtn[row][col]=='0':
            # print(f"=======now starting probe with {row},{col}")
            visited = [[False for i in range(len(mtn[0]))] for j in range(len(mtn))]
            score_sum += score(row, col)

print(score_sum)