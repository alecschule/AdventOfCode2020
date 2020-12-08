with open('input.txt') as f:
    groups = f.read().split('\n\n')
    count = 0
    for group in groups:
        lines = group.split('\n')
        letterSet = set(lines[0])
        for line in lines[1:]:
            letterSet = letterSet.intersection(set(line))
        count += len(letterSet)
    print(count)
