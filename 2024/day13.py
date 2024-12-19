import re

pattern = r'Button A: X\+([0-9]+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'

with open("day13_input.txt") as file:
    machines = re.findall(pattern,file.read())

print(machines)
# print(machs)

#wait this is linear algebra

def cost_to_win(A_x, A_y, B_x, B_y, goal_x, goal_y):

    A_count = 0
    B_count = 0

    while ((A_count*A_x + B_count*B_x)!=goal_x or (A_count*A_y + B_count*B_y)!=goal_y):
        pass

    return A_count*3 + B_count

cost = 0

for machine in machines:
    machine = [int(i) for i in machine]
    print(machine)
    # A_x, A_y, B_x, B_y = machine[0], machine[1], machine[2], machine[3]
    # goal_x, goal_y = machine[4], machine[5]
    cost += cost_to_win(*machine)

print(cost)