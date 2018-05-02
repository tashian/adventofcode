import utils
from operator import add, sub
from collections import defaultdict
from day1 import next_orientation, orientation_op

path = "L3, R1, L4, L1, L2, R4, L3, L3, R2, R3, L5, R1, R3, L4, L1, L2, R2, R1, L4, L4, R2, L5, R3, R2, R1, L1, L2, R2, R2, L1, L1, R2, R1, L3, L5, R4, L3, R3, R3, L5, L190, L4, R4, R51, L4, R5, R5, R2, L1, L3, R1, R4, L3, R1, R3, L5, L4, R2, R5, R2, L1, L5, L1, L1, R78, L3, R2, L3, R5, L2, R2, R4, L1, L4, R1, R185, R3, L4, L1, L1, L3, R4, L4, L1, R5, L5, L1, R5, L1, R2, L5, L2, R4, R3, L2, R3, R1, L3, L5, L4, R3, L2, L4, L5, L4, R1, L1, R5, L2, R4, R2, R3, L1, L1, L4, L3, R4, L3, L5, R2, L5, L1, L1, R2, R3, L5, L3, L2, L1, L4, R4, R4, L2, R3, R1, L2, R1, L2, L2, R3, R3, L1, R4, L5, L3, R4, R4, R1, L2, L5, L3, R1, R4, L2, R5, R4, R2, L5, L3, R4, R1, L1, R5, L3, R1, R5, L2, R1, L5, L2, R2, L2, L3, R3, R3, R1"
path = [[t[0], int(t[1::])] for t in path.split(", ")]

visited = defaultdict(int)

def steps(x, y, orientation, dist):
    for i in range(dist):
        if orientation == 'E' or orientation == 'W':
            x = orientation_op(orientation)(x, 1)
        else:
            y = orientation_op(orientation)(y, 1)
        yield x, y

def walk(x, y, orientation, dist):
    for x, y in steps(x, y, orientation, dist):
        if (x, y) in visited:
            print("Crossed at {}, {}".format(x, y))
            exit()
        visited[x, y] = True
    return visited

def find_first_cross(path):
    x, y = 0, 0
    orientation = "N"
    for turn, dist in path:
        orientation = next_orientation(orientation, turn)
        walk(x, y, orientation, dist)
        x, y = list(visited.keys())[-1]

print(find_first_cross(path))
