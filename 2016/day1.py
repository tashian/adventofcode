import utils
import operator

path = "L3, R1, L4, L1, L2, R4, L3, L3, R2, R3, L5, R1, R3, L4, L1, L2, R2, R1, L4, L4, R2, L5, R3, R2, R1, L1, L2, R2, R2, L1, L1, R2, R1, L3, L5, R4, L3, R3, R3, L5, L190, L4, R4, R51, L4, R5, R5, R2, L1, L3, R1, R4, L3, R1, R3, L5, L4, R2, R5, R2, L1, L5, L1, L1, R78, L3, R2, L3, R5, L2, R2, R4, L1, L4, R1, R185, R3, L4, L1, L1, L3, R4, L4, L1, R5, L5, L1, R5, L1, R2, L5, L2, R4, R3, L2, R3, R1, L3, L5, L4, R3, L2, L4, L5, L4, R1, L1, R5, L2, R4, R2, R3, L1, L1, L4, L3, R4, L3, L5, R2, L5, L1, L1, R2, R3, L5, L3, L2, L1, L4, R4, R4, L2, R3, R1, L2, R1, L2, L2, R3, R3, L1, R4, L5, L3, R4, R4, R1, L2, L5, L3, R1, R4, L2, R5, R4, R2, L5, L3, R4, R1, L1, R5, L3, R1, R5, L2, R1, L5, L2, R2, L2, L3, R3, R3, R1"

def next_orientation(orientation, turn):
    return {("N", "L"): "W", ("S", "R"): "W",
                   ("N", "R"): "E", ("S", "L"): "E",
                   ("E", "L"): "N", ("W", "R"): "N",
                   ("W", "L"): "S", ("E", "R"): "S"}[(orientation, turn)]

def orientation_op(orientation):
    return {'N': operator.add, 'S': operator.sub,
        'E': operator.add, 'W': operator.sub}[orientation]

def blocks_away(path, orientation):
    path = [[t[0], int(t[1::])] for t in path.split(", ")]
    x, y = 0, 0
    for turn in path:
        orientation = next_orientation(orientation, turn[0])
        if orientation == 'E' or orientation == 'W':
            x = orientation_op(orientation)(x, turn[1])
        else:
            y = orientation_op(orientation)(y, turn[1])

    return abs(x) + abs(y)

assert(blocks_away("R2, L3", "N") == 5)
assert(blocks_away("R2, R2, R2", "N") == 2)
assert(blocks_away("R5, L5, R5, R3", "N") == 12)
print(blocks_away(path, "N"))
