test_directions = """ULL
RRDDD
LURDL
UUUUD"""

with open("day2.txt") as f:
    directions = f.read()

keys = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def print_code(keys, directions, start):
    x, y = start
    edge = len(keys) - 1
    for steps in directions.split():
        for step in steps:
            xn, yn = x, y
            if step == "U":
                yn = max(0, y-1)
            if step == "D":
                yn = min(edge, y+1)
            if step == "R":
                xn = min(edge, x+1)
            if step == "L":
                xn = max(0, x-1)
            if keys[xn][yn]:
                x, y = xn, yn
        print(keys[y][x])

print_code(keys, directions, (1, 1))
print()

keys = [[None, None,   1, None, None],
        [None,    2,   3,    4, None],
        [5   ,    6,   7,    8,    9],
        [None,  'A', 'B',  'C', None],
        [None, None, 'D', None, None]]

print_code(keys, directions, (2, 0))
