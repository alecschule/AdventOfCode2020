numbers = [0]
with open("input.txt") as f:
    for i in f.read().splitlines():
        numbers.append(int(i))
numbers.sort()
numbers.append(numbers[-1] + 3)

# part 2
counts = [0] * len(numbers)
counts[-1] = 1
for i in reversed(range(len(numbers) - 1)):
    counts[i] = sum(counts[i+j] for j in range(1, 4) if i+j < len(numbers) and numbers[i+j] - numbers[i] <= 3)

print(counts[0])
