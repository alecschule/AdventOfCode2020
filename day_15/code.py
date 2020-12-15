with open('input.txt') as f:
    numbers = [int(i) for i in f.read().split(',')]

hist = {i: index+1 for index,i in enumerate(numbers)}
num = 0
for i in range(len(numbers) + 1, 30000000):
    old_num = num
    num = i - hist[num] if num in hist else 0
    hist[old_num] = i

print(num)
