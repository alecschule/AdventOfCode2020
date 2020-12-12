from copy import deepcopy
with open('input.txt') as f:
    seatmap = [list(l) for l in f.read().splitlines()]

def advance_tick(seatmap):
    temp_seatmap = deepcopy(seatmap)
    return_val = False
    for y, row in enumerate(seatmap):
        for x, column in enumerate(row):
            visible_seats = []
            # up left
            for i in range(1, min(x, y) + 1):
                if temp_seatmap[y-i][x-i] != '.':
                    visible_seats.append(temp_seatmap[y-i][x-i])
                    break
            # up
            for i in range(1, y+1):
                if temp_seatmap[y-i][x] != '.':
                    visible_seats.append(temp_seatmap[y-i][x])
                    break
            # up right
            for i in range(1, min(y+1, len(temp_seatmap[0]) - x)):
                if temp_seatmap[y-i][x+i] != '.':
                    visible_seats.append(temp_seatmap[y-i][x+i])
                    break
            # left
            for i in range(1, x+1):
                if temp_seatmap[y][x-i] != '.':
                    visible_seats.append(temp_seatmap[y][x-i])
                    break
            # right
            for i in range(1, len(temp_seatmap[0]) - x):
                if temp_seatmap[y][x+i] != '.':
                    visible_seats.append(temp_seatmap[y][x+i])
                    break
            # down left
            for i in range(1, min(len(temp_seatmap) - y, x+1)):
                if temp_seatmap[y+i][x-i] != '.':
                    visible_seats.append(temp_seatmap[y+i][x-i])
                    break
            # down
            for i in range(1, len(temp_seatmap) - y):
                if temp_seatmap[y+i][x] != '.':
                    visible_seats.append(temp_seatmap[y+i][x])
                    break
            # down right
            for i in range(1, min(len(temp_seatmap) - y, len(temp_seatmap[0]) - x)):
                if temp_seatmap[y+i][x+i] != '.':
                    visible_seats.append(temp_seatmap[y+i][x+i])
                    break
            if column == 'L':
# part1                if all(temp_seatmap[i][j] != '#' for i in [y-1, y, y+1] for j in [x-1, x, x+1] if 0 <= i < len(seatmap) and 0 <= j < len(seatmap[0])):
                if all(seat != '#' for seat in visible_seats):
                    seatmap[y][x] = '#'
                    return_val = True
            elif column == '#':
# part1                if [temp_seatmap[i][j] == '#' for i in [y-1, y, y+1] for j in [x-1, x, x+1] if 0 <= i < len(seatmap) and 0 <= j < len(seatmap[0]) and not (i == y and j == x)].count(True) >= 4:
                if [seat == '#' for seat in visible_seats].count(True) >= 5:
                    seatmap[y][x] = 'L'
                    return_val = True
    return return_val

while(advance_tick(seatmap)): pass
print([seat == '#' for row in seatmap for seat in row].count(True))
