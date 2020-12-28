import re
from itertools import chain

with open('input.txt') as f:
    lines = f.read().splitlines()

allergy_map = {}
all_ingredients = []
for line in lines:
    search = re.match("^(.*) \(contains (.*)\)$", line)
    ingredients = search.group(1).split(' ')
    allergens = search.group(2).split(', ')
    for allergen in allergens:
        allergy_map[allergen] = allergy_map[allergen] & set(ingredients) if allergen in allergy_map else set(ingredients)
    all_ingredients.extend(ingredients)

# part 1
possible_allergens = set(chain(*allergy_map.values()))
not_allergens = set(all_ingredients) - possible_allergens
# print(sum(all_ingredients.count(ingredient) for ingredient in not_allergens))

# part 2
while(any(len(i) > 1 for i in allergy_map.values())):
    for key, value in allergy_map.items():
        if (len(value) == 1):
            ingredient = next(iter(value))
            for key_b, value_b in allergy_map.items():
                if key != key_b and ingredient in value_b: value_b.remove(ingredient)

print(",".join(next(iter(allergy_map[i])) for i in sorted(allergy_map.keys())))
