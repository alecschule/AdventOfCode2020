SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open('input.txt') as f:
    lines = f.readlines()
    grid = [list(line.rstrip()) for line in lines]
    product = 1
    for SLOPE_X, SLOPE_Y in SLOPES:
        count = x = y = 0
        while y <= len(grid):
            count += grid[y][x] == '#'
            x = (x + SLOPE_X) % len(grid[0])
            y += SLOPE_Y
            if y >= len(grid):
                break
        product *= count
    print(product)
