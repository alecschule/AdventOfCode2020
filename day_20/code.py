import re

dimension = 12
with open('input.txt') as f:
    data = f.read()

# each tile has [id, text, neighbors (in original orientation), orientation]
tiles = []
for tile in data.split('\n\n'):
    parts = tile.split('\n', 1)
    t_id = re.search("\d+", parts[0]).group(0)
    tiles.append([int(t_id), parts[1].splitlines(), [None]*4, None])

def get_borders(tile):
    # in NESW order
    return [tile[0],
            "".join([line[-1] for line in tile]),
            tile[-1],
            "".join([line[0] for line in tile])]

borders = [get_borders(tile[1]) for tile in tiles]
for index, i in enumerate(borders):
    for b_index, border in enumerate(i):
        found_neighbor = False
        for j_index, j in enumerate(borders):
            if index == j_index: continue
            for j_border in j: 
                if border == j_border or border == j_border[::-1]: 
                    found_neighbor = True
                    tiles[index][2][b_index] = tiles[j_index][0]
        if not found_neighbor:
            tiles[index][2][b_index] = -1 # -1 represents map edge

# part 1
prod = 1
for tile in tiles:
    if tile[2].count(-1) == 2: prod *= tile[0]
# print(prod)

# part 2
def get_interior(tile_text):
    return [line[1:-1] for line in tile_text[1:-1]]

def find_orientation(neighbors, needed_neighbors):
    index_list = [index for index, neighbor in enumerate(needed_neighbors) if neighbor is not None]
    # align first neighbor by rotation
    current_index = neighbors.index(needed_neighbors[index_list[0]])
    rotation = (4 - (current_index-index_list[0])) % 4
    # flip to align second neighbor if needed
    current_index = [i for i,x in enumerate(neighbors) if x == needed_neighbors[index_list[1]]][-1]
    adjusted_index = (current_index+rotation) % 4
    if adjusted_index != index_list[1]:
        # flip needed 1 = horizontal 2 = vertical
        reflection = 1 if adjusted_index % 2 == 1 else 2
    else: reflection = 0
    return (rotation, reflection)

# build a map of image ids
space = [[None] * dimension for i in range(dimension)]
last_tile = [tile for tile in tiles if tile[2].count(-1) == 2][0]
space[0][0] = last_tile[0]
orientation = find_orientation(last_tile[2], [-1, None, None, -1])
last_tile[3] = orientation
for i in range(dimension):
    if i != 0:
        above_tile = [tile for tile in tiles if tile[0] == space[i-1][0]][0]
        bot_index = (6 - above_tile[3][0]) % 4
        if above_tile[3][1] == 2: bot_index = (bot_index + 2) % 4
        space[i][0] = above_tile[2][bot_index]
        last_tile = [tile for tile in tiles if tile[0] == space[i][0]][0]
        orientation = find_orientation(last_tile[2], [above_tile[0], None, None, -1])
        last_tile[3] = orientation
    for j in range(1, dimension):
        # tile to the right after orienting
        right_index = (5 - orientation[0]) % 4
        if orientation[1] == 1: right_index = (right_index + 2) % 4
        space[i][j] = last_tile[2][right_index]
        above_tile = -1 if i == 0 else space[i-1][j]
        new_tile = [tile for tile in tiles if tile[0] == space[i][j]][0]
        orientation = find_orientation(new_tile[2], [above_tile, None, None, last_tile[0]])
        new_tile[3] = orientation
        last_tile = new_tile

# find sea monsters
# build image
def rotate(inpt, degree):
    result = inpt
    for i in range(degree):
        result = list(zip(*result[::-1]))
    return ["".join(i) for i in result]

def v_reflect(inpt):
    return inpt[::-1]

def h_reflect(inpt):
    return [i[::-1] for i in inpt]

image = []
for image_index, i in enumerate(space):
    for j in i:
        tile = [tile for tile in tiles if tile[0] == j][0]
        interior = get_interior(tile[1])
        interior = rotate(interior, tile[3][0])
        if tile[3][1] == 1: interior = h_reflect(interior)
        elif tile[3][1] == 2: interior = v_reflect(interior)
        for tile_index, k in enumerate(interior):
            if len(image) <= image_index*len(interior)+tile_index: image.append(k)
            else: image[image_index*len(interior)+tile_index] += k

# search image
monster_text = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
monster_regex = [f"(?=({i.replace(' ', '.')}))" for i in monster_text]
monster_count = 0
for reflect_image in [image, h_reflect(image), v_reflect(image)]:
    for i in range(4):
        rotate_image = rotate(reflect_image, i)
        for j in range(len(rotate_image)-2):
            matches = {m.start(0) for m in re.finditer(monster_regex[0], rotate_image[j])}
            matches = matches & {m.start(0) for m in re.finditer(monster_regex[1], rotate_image[j+1])}
            matches = matches & {m.start(0) for m in re.finditer(monster_regex[2], rotate_image[j+2])}
            monster_count += len(matches)
        if monster_count > 0: break
    if monster_count > 0: break

monster_pieces = monster_count * sum(i.count('#') for i in monster_text)
water_roughness = sum(i.count('#') for i in image)
print(water_roughness - monster_pieces)
