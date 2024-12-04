search = []

with open("day4_input.txt") as file:
    for line in file:
        search.append(line.strip())

count = 0

def vertical(i, j):
    count = 0

    if (i>=3 and 
        (search[i][j]=='X' and 
         search[i-1][j]=='M' and
         search[i-2][j]=='A' and
         search[i-3][j]=='S'
         )):
        count += 1

    if ( i<=len(search)-4 and
        (search[i][j]=='X' and 
         search[i+1][j]=='M' and
         search[i+2][j]=='A' and
         search[i+3][j]=='S'
        )):
        count += 1
    
    return count

def horizontal(i, j):
    count = 0

    if (j>=3 and 
        (search[i][j]=='X' and 
         search[i][j-1]=='M' and 
         search[i][j-2]=='A' and 
         search[i][j-3]=='S')):
        count += 1
        
    if ( j<=len(search[i])-4 and 
        (search[i][j]=='X' and 
         search[i][j+1]=='M' and 
         search[i][j+2]=='A' and 
         search[i][j+3]=='S')):
        count += 1
    
    return count

def diagonal(i, j):
    count = 0

    if (i>=3 and j>=3 and 
        (search[i][j]=='X' and 
         search[i-1][j-1]=='M' and
         search[i-2][j-2]=='A' and
         search[i-3][j-3]=='S'
         )):
        count += 1
        
    if (i>=3 and j<=len(search[i])-4 and 
        (
        search[i][j]=='X' and 
         search[i-1][j+1]=='M' and
         search[i-2][j+2]=='A' and
         search[i-3][j+3]=='S'
        )):
        count += 1
    
    if (i<=len(search)-4 and j>=3 and
       (search[i][j]=='X' and 
         search[i+1][j-1]=='M' and
         search[i+2][j-2]=='A' and
         search[i+3][j-3]=='S'
        )):
        count += 1
        
    if (i<=len(search)-4 and j<=len(search[i])-4 and 
        (search[i][j]=='X' and 
         search[i+1][j+1]=='M' and
         search[i+2][j+2]=='A' and
         search[i+3][j+3]=='S'
        )):
        count += 1
    
    return count

for i in range(len(search)):
    for j in range(len(search[i])):
        if search[i][j]=='X':
            count += vertical(i, j) + horizontal(i, j) + diagonal(i, j)

print("part 1")
print(count)

count = 0

def mas(i, j):

    count = 0

    if (
        (
            (search[i-1][j-1]=='M' and 
             search[i][j]=='A' and 
             search[i+1][j+1]=='S'
             ) 
             or 
             (search[i+1][j+1]=='M' and 
             search[i][j]=='A' and 
             search[i-1][j-1]=='S'
             )
         ) and 
        (
            (search[i-1][j+1]=='M' and 
             search[i][j]=='A' and 
             search[i+1][j-1]=='S'  
            ) or (
            search[i+1][j-1]=='M' and 
             search[i][j]=='A' and 
             search[i-1][j+1]=='S' 
            )
        )
    ):
        count += 1
    
    return count

for i in range(1, len(search)-1):
    for j in range(1, len(search[i])-1):
        if search[i][j]=='A':
            count += mas(i, j)

print("part 2")
print(count)