from collections import Counter
import time

start_time = time.time()

with open("day11_input.txt") as file:
    stones = Counter([int(i) for i in file.read().strip().split(" ")])

# stones = Counter([125, 17])

print(stones)

def blink(stones):

    new_stones = Counter()

    for stone,count in stones.items():

        if stone==0:
            new_stones[1]+= count
        elif len(str(stone))%2==0:
            s = str(stone)
            mid = len(s)//2
            f = int(s[:mid])
            s = int(s[mid:])
            new_stones[f] += count
            new_stones[s] += count
        else:
            new_stones[stone*2024] += count
        
    return new_stones

for i in range(25):
    stones = blink(stones)

print(sum(list(stones.values())))

for i in range(50):
    stones = blink(stones)

end_time = time.time()

print(sum(list(stones.values())))
print(end_time-start_time)