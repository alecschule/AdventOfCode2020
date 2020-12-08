from copy import deepcopy 
with open("input.txt") as f:
    lines = f.read().splitlines()
    program = list(map(lambda l: {"count": 0, "instruction": [l.split(' ')[0], int(l.split(' ')[1])]}, lines))

def check_program(program):
    current_line = 0
    acc = 0
    while True:
        if current_line == len(program):
            return acc
        if program[current_line]["count"] > 0:
            return None
        program[current_line]["count"] += 1
        if program[current_line]["instruction"][0] == "acc":
            acc += program[current_line]["instruction"][1]
        if program[current_line]["instruction"][0] == "jmp":
            current_line += program[current_line]["instruction"][1]
        else:
            current_line += 1

for i in range(len(program)):
    temp_program = deepcopy(program)
    instruction = temp_program[i]["instruction"]
    if instruction[0] in ["nop", "jmp"]:
        instruction[0] = "nop" if instruction[0] == "jmp" else "jmp"
    result = check_program(temp_program)
    if result:
        print(result)
        break
