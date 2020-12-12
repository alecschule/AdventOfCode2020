import math

with open('input.txt') as f:
    lines = f.read().splitlines()

ew = 10 # waypoint east-west coordinate
ns = -1 # waypoint north-south coordinate
ship_ew = 0
ship_ns = 0
for line in lines:
    direction = line[0]
    degree = int(line[1:])
    if direction in ['R', 'L']:
        ns_multiplier = 1 if direction == 'R' else -1
        ew_multiplier = -1 if direction == 'R' else 1
        old_ew = ew
        old_ns = ns
        ew = old_ns * ew_multiplier * int(math.sin(math.radians(degree))) + old_ew * int(math.cos(math.radians(degree)))  
        ns = old_ew * ns_multiplier * int(math.sin(math.radians(degree))) + old_ns * int(math.cos(math.radians(degree)))  
    elif direction == 'N':
        ns -= degree
    elif direction == 'S':
        ns += degree
    elif direction == 'E':
        ew += degree
    elif direction == 'W':
        ew -= degree
    else: # F
        ship_ew += ew * degree
        ship_ns += ns * degree

print(abs(ship_ew) + abs(ship_ns))
