with open ('input.txt') as f:
    parts = f.read().split('\n\n')

values = {line.split(': ')[0]: [(int(value.split('-')[0]), int(value.split('-')[1])) for value in line.split(': ')[1].split(' or ')] for line in parts[0].splitlines()}


valid = lambda i: any(any(bottom <= i <= top for bottom, top in field) for field in values.values())

# part 1
scanning_error = sum(sum(int(i) for i in ticket.split(',') if not valid(int(i))) for ticket in parts[2].splitlines()[1:])
# print(scanning_error)

# part 2
valid_tickets = [[int(i) for i in line.split(',')] for line in parts[2].splitlines()[1:] if all(valid(int(value)) for value in line.split(','))]

field_map = {}
for field, value in values.items():
    field_map[field] = [i for i in range(len(valid_tickets[0])) if all(any(bottom <= ticket[i] <= top for bottom, top in value) for ticket in valid_tickets)]

while any(len(i) > 1 for i in field_map.values()):
    for field, value in field_map.items():
        if len(value) == 1:
            for field_a in field_map.keys():
                if field != field_a and value[0] in field_map[field_a]:
                    field_map[field_a].remove(value[0])

my_ticket = [int(i) for i in parts[1].split('\n')[1].split(',')]

answer = 1
for field in values.keys():
    if field.startswith('departure'):
        answer *= my_ticket[field_map[field][0]]

print(answer)
