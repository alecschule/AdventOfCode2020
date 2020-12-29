import re
from itertools import chain

with open('input.txt') as f:
    lines = f.read().splitlines()

grid = {}
for line in lines:
    directions = re.split("(nw|ne|sw|se|w|e)", line)[1::2]
    ne_coor = len([i for i in directions if i in ['ne', 'e']]) - len([i for i in directions if i in ['sw', 'w']])
    se_coor = len([i for i in directions if i in ['se', 'e']]) - len([i for i in directions if i in ['nw', 'w']])
    if ne_coor in grid:
        if se_coor in grid[ne_coor]: grid[ne_coor][se_coor] = not grid[ne_coor][se_coor]
        else: grid[ne_coor][se_coor] = False
    else: grid[ne_coor] = {se_coor: False}

# part 1
# print(sum([i for i in j.values()].count(False) for j in grid.values()))

# part 2
min_ne = min(i for i in grid)
max_ne = max(i for i in grid)
min_se = min(min(i for i in j) for j in grid.values())
max_se = max(max(i for i in j) for j in grid.values())

# fill grid
for i in range(min_ne-101, max_ne+101):
    if not i in grid: grid[i] = {}
    for j in range(min_se-101, max_se+101):
        if not j in grid[i]: grid[i][j] = True

for i in range(100):
    to_change = []
    for ne_coor in range(min_ne-100, max_ne+100):
        se_line = grid[ne_coor]
        for se_coor in range(min_se-100, max_se+100):
            neighbors = [grid[x][y] for x,y in [(ne_coor, se_coor-1), (ne_coor, se_coor+1), (ne_coor-1, se_coor), (ne_coor+1, se_coor), (ne_coor+1, se_coor+1), (ne_coor-1, se_coor-1)]]
            b_neighbors = neighbors.count(False)
            if not grid[ne_coor][se_coor] and not 0 < b_neighbors <= 2: to_change.append((ne_coor, se_coor, True))
            if grid[ne_coor][se_coor] and b_neighbors == 2: to_change.append((ne_coor, se_coor, False))
    for x, y, val in to_change:
        grid[x][y] = val

print(sum([i for i in j.values()].count(False) for j in grid.values()))
