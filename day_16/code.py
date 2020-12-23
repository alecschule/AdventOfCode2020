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
for field in values.keys():
    for i in range(len(valid_tickets[0])):
        if all(

print(valid_tickets)
