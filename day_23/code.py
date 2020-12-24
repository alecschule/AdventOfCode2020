inpt = "974618352"
num_cups = 1000000
moves = 10000000

cups = {}
for i in range(len(inpt)- 1):
    cups[int(inpt[i])] = int(inpt[i+1])
for i in range(len(inpt)+1, num_cups):
    cups[i] = i+1
if num_cups > len(inpt):
    cups[int(inpt[-1])] = len(inpt) + 1
    cups[num_cups] = int(inpt[0])
else:
    cups[int(inpt[-1])] = int(inpt[0])

current = int(inpt[0])
for i in range(moves):
    after = cups[current]
    two_after = cups[after]
    three_after = cups[two_after]
    four_after = cups[three_after]
    cups[current] = four_after
    destination = current - 1
    while destination in [0, after, two_after, three_after]:
        destination -= 1
        if destination < 0: destination = num_cups
    destination_after = cups[destination]
    cups[destination] = after
    cups[three_after] = destination_after
    current = cups[current]

def part_one():
    global cups
    printer = 1
    for i in range(num_cups-1):
        printer = cups[printer]
        print(printer, end='')
    print()

def part_two():
    global cups
    print(cups[1] * cups[cups[1]])

# part_one()
part_two()
