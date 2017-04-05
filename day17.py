# No Such Thing as Too Much
# http://adventofcode.com/2015/day/17

CONTAINER_SIZES = [
    50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40
]

EGGNOG_VOLUME = 150

# Notes:
# This will require between 4 and 8 containers.
from itertools import combinations, ifilter

combos = 0
for i in range(4, 9):
    combos = len(list(ifilter(lambda x: sum(x) == EGGNOG_VOLUME, combinations(CONTAINER_SIZES, i))))
    print combos, "combinations if you use", i, "containers"

