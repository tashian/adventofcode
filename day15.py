# Cookie-dunking.
#
# Goals:
# - Find a ratio of ingredients that maximizes the total cookie score.
# - Total must be 100 teaspoons of ingredients.
# - Input includes how each ingredient affects the properties of the cookie:
# Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
# Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
# Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
# Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
from itertools import ifilter, permutations

PART_ONE = True

INGREDIENTS = [[2, 0, -2, 0],
              [0, 5, -3, 0],
              [0, 0, 5, -1],
              [0, -1, 0, 5]]

INGREDIENTS_BY_PROPERTY = list(zip(*INGREDIENTS))

CALORIES_PER_INGREDIENT = [3, 3, 8, 8]

def score_one_option(ratios):
    score = 1
    for properties in INGREDIENTS_BY_PROPERTY:
        property_total = 0
        for i, p in enumerate(properties):
            property_total += p*ratios[i]
        if property_total < 0:
            property_total = 0
        score *= property_total
    return score

def calories(ratios):
    total_calories = 0
    for i, ratio in enumerate(ratios):
        total_calories += CALORIES_PER_INGREDIENT[i]*ratio
    return total_calories

def acceptable_permutation(ratios):
    return sum(ratios) == 100 and (PART_ONE or calories(ratios) == 500)

max_score = 0
for ratios in ifilter(acceptable_permutation, permutations(range(1,99), 4)):
    score = score_one_option(ratios)
    if score > max_score:
        max_score = score
        print max_score, ratios

print max_score
