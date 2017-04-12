# Infinite Elves and Infinite Houses
import sys
import utils

def presents_for_house(n):
    presents = 0
    for elf in utils.factors(n):
        presents += elf * 10
    return presents

assert(presents_for_house(1) == 10)
assert(presents_for_house(2) == 30)
assert(presents_for_house(3) == 40)
assert(presents_for_house(4) == 70)
assert(presents_for_house(5) == 60)
assert(presents_for_house(6) == 120)
assert(presents_for_house(7) == 80)
assert(presents_for_house(8) == 150)
assert(presents_for_house(9) == 130)

house = 10
presents = 0
while presents < 29000000:
   # Hunch: The answer will be divisible by 10
   house += 10
   presents = presents_for_house(house)

print house
