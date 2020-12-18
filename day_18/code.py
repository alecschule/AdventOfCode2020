import re

with open('input.txt') as f:
    lines = f.read().splitlines()

def evaluate(string):
    while string.find('(') != -1:
        left = string[:string.rfind('(')]
        middle = string[string.rfind('(')+1:string.find(')', string.rfind('('))]
        right = string[string.find(')', string.rfind('('))+1:]
        string = left + evaluate(middle) + right
    if string.count(' ') == 0: return string
    while string.count('+') > 0:
        parts = re.split("(\d+ \+ \d+)", string, 1)
        string = parts[0] + str(eval(parts[1])) + parts[2]
    while string.count('*') > 0:
        parts = re.split("(\d+ \* \d+)", string, 1)
        string = parts[0] + str(eval(parts[1])) + parts[2]
    return string

print(sum(int(evaluate(l)) for l in lines))
