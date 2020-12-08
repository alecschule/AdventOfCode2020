containers = {}
with open('input.txt') as f:
    for line in f.read().splitlines():
        container = line.split(' contain ')[0][:-5]
        contents = []
        for item in line.split(' contain ')[1].split(', '):
            trimmedItem = item[:item.rindex(' ')]
            if trimmedItem == 'no other':
                continue
            contents.append([int(trimmedItem[:trimmedItem.index(' ')]), trimmedItem[trimmedItem.index(' ')+1:]])
        containers[container] = contents

def canContain(container, content):
    if any([content == x[1] for x in containers[container]]):
        return True
    return any(canContain(x[1], content) for x in containers[container])

def contents(container):
    return 1 + sum(x[0]*contents(x[1]) for x in containers[container])

# part 1
# print(sum(canContain(x, "shiny gold") for x in containers.keys()))

# part 2
print(contents("shiny gold") - 1) # -1 for the shiny gold bag itself
