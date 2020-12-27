import re

with open('input.txt') as f:
    parts = f.read().split('\n\n')

rules = {line.split(': ')[0]: line.split(': ')[1] for line in parts[0].splitlines()}
messages = parts[1].splitlines()

def find_matches(rule):
    global rules
    options = rule.split(' | ')
    if len(options) == 1:
        parts = rule.split(' ')
        if len(parts) == 1:
            if rule[0] == '"': return {rule[1:-1]} 
            else: return find_matches(rules[rule])
        partial_matches = [find_matches(part) for part in parts]
        matches = partial_matches[0]
        for x in partial_matches[1:]:
            temp = {a+b for a in matches for b in x}
            matches = temp
        return matches
    matches = set()
    for option in options:
        matches.update(find_matches(option))
    return matches

# part 1
matches = find_matches("0")
print([message in matches for message in messages].count(True))

# part 2
# rules["0"] = "8 11"
# rules["8"] = "42 | 42 8"
# rules["11"] = "42 31 | 42 11 31"
# minimum 42 42 31
# at least two 42 followed by at most one fewer 31

ft_matches = find_matches("42")
to_matches = find_matches("31")
regex_init = f"^(?:{'|'.join([i for i in ft_matches])}){{2}}(.*?)(?:{'|'.join([i for i in to_matches])}){{1}}$"
regex = f"^(?:{'|'.join([i for i in ft_matches])})(.*?)(?:{'|'.join([i for i in to_matches])})?$"
count = 0
for message in messages:
    match = re.match(regex_init, message)
    while match is not None:
        temp = match.group(1)
        if len(temp) == 0:
            count += 1
            break
        match = re.match(regex, temp)

print(count)
