with open('input.txt') as f:
    lines = f.read().splitlines()

space = {0: {0 : {i: {j: char for j, char in enumerate(line)} for i, line in enumerate(lines)}}}
low_x = 0
high_x = len(lines) - 1
low_y = 0
high_y = len(lines[0]) - 1
low_z = 0
high_z = 0
low_w = 0
high_w = 0

def print_space():
    global space, low_w, high_w, low_x, high_x, low_y, high_y, low_z, high_z
    for w in range(low_w, high_w+1):
        for z in range(low_z, high_z+1):
            print('z=', z, ' w=', w, sep='')
            for x in range(low_x, high_x+1):
                for y in range(low_y, high_y+1):
                    print(space[w][z][x][y], end='')
                print()

for i in range(6):
    low_x -= 1
    high_x += 1
    low_y -= 1
    high_y += 1
    low_z -= 1
    high_z += 1
    low_w -= 1
    high_w += 1
    space[low_w] = {k: {i: {j: '.' for j in range(low_y, high_y+1)} for i in range(low_x, high_x+1)} for k in range(low_z, high_z+1)}
    space[high_w] = {k: {i: {j: '.' for j in range(low_y, high_y+1)} for i in range(low_x, high_x+1)} for k in range(low_z, high_z+1)}
    for w in range(low_w + 1, high_w):
        space[w][low_z] = {i: {j: '.' for j in range(low_y, high_y + 1)} for i in range(low_x, high_x + 1)}
        space[w][high_z] = {i: {j: '.' for j in range(low_y, high_y + 1)} for i in range(low_x, high_x + 1)}
        for z in range(low_z + 1, high_z):
            space[w][z][low_x] = {}
            space[w][z][high_x] = {}
            for i in range(low_y, high_y + 1):
                space[w][z][low_x][i] = '.'
                space[w][z][high_x][i] = '.'
            for i in range(low_x + 1, high_x):
                space[w][z][i][low_y] = '.'
                space[w][z][i][high_y] = '.'
    to_change = []
    for h in range(low_w, high_w+1):
        for i in range(low_z, high_z+1):
            for j in range(low_x, high_x+1):
                for k in range(low_y, high_y+1):
                    neighbors = [space[w][z][x][y]
                            for w in range(max(h-1, low_w), min(h+1, high_w)+1)
                            for z in range(max(i-1, low_z), min(i+1, high_z)+1)
                            for x in range(max(j-1, low_x), min(j+1, high_x)+1)
                            for y in range(max(k-1, low_y), min(k+1, high_y)+1)
                            if not (w == h and i == z and j == x and k == y)]
                    if space[h][i][j][k] == '#' and not 2 <= neighbors.count('#') <= 3: to_change.append([h, i, j, k, '.'])
                    elif space[h][i][j][k] == '.' and neighbors.count('#') == 3: to_change.append([h, i, j, k, '#'])
    for i in to_change:
        space[i[0]][i[1]][i[2]][i[3]] = i[4]

print([space[h][i][j][k] for h in range(low_w, high_w+1) for i in range(low_z, high_z+1) for j in range(low_x, high_x+1) for k in range(low_y, high_y+1)].count('#'))
