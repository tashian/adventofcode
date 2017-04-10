# Infinite Elves and Infinite Houses
import sys

def presents_for_house(n):
    presents = 0
    for elf in factors(n):
        presents += elf * 10
    return presents

# Fast factoring via http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

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
