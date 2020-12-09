from queue import Queue
with open("input.txt") as f:
    lines = f.read().splitlines()
    history = Queue()
    for line in lines[:25]:
        history.put(int(line))
    for line in lines[25:]:
        if not any(x + y == int(line) for i,x in enumerate(history.queue) for j,y in enumerate(history.queue) if i != j):
            invalid = int(line)
            break
        history.get()
        history.put(int(line))

    for i, line in enumerate(lines):
        temp_sum = int(line)
        numbers = [int(line)]
        for line_b in lines[i+1:]:
            temp_sum += int(line_b)
            numbers.append(int(line_b))
            if temp_sum == invalid:
                print(min(numbers) + max(numbers))
            if temp_sum > invalid:
                break
