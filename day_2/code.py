f = open('input.txt')

result = 0
for line in f:
    parts = line.split(' ')
    mini = int(parts[0].split('-')[0])
    maxi = int(parts[0].split('-')[1])
    letter = parts[1][0]
    string = parts[2]
    count = string.count(letter)
    if (string[mini-1] == letter and string[maxi-1] != letter) or (string[mini-1] != letter and string[maxi-1] == letter):
        result += 1

print(result)
