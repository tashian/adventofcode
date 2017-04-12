# Infinite Elves and Infinite Houses part 2
# 1119195 is too high.

import utils
import sys
from collections import deque, defaultdict

class Elf:
    def __init__(self):
        self.visits = 0

    def give_presents(self, n):
        if self.visits < 50:
            self.visits += 1
            return 11 * n
        else:
            return 0

house = 1
elf = defaultdict(Elf)
presents = 0
while presents < 29000000:
   house += 1
   presents = 0
   for i in utils.factors(house):
       presents += elf[i].give_presents(i)
   if house % 100000 == 0:
       print house, presents

print house, presents

