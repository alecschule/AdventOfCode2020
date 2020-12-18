with open('input.txt') as f:
    lines = f.read().splitlines()

mem = {}
for line in lines:
    parts = line.split(' = ')
    if parts[0] == 'mask':
        mask = parts[1]
    else:
        addr = int(parts[0][4:-1])
        addr = addr | int(mask.replace('X', '0'), 2)
        indeces = []
        for index, c in enumerate(reversed(mask)):
            if c == 'X': indeces.append(index)
        x_count = mask.count('X')
        for i in range(2 ** x_count):
            temp_addr = addr
            for j in range(x_count):
                active_bit = (i & 1 << j) >> j
                if active_bit == 0: temp_addr = temp_addr & ~(1<<indeces[j])
                else: temp_addr = temp_addr | (1 << indeces[j])
            mem[temp_addr] = int(parts[1])

print(sum(value for value in mem.values()))
