from collections import defaultdict

with open('day3.txt', 'r') as day3:
    directions = day3.read()

def move(turn, loc):
    if turn == '>':
        loc[0] += 1
    elif turn == '<':
        loc[0] -= 1
    elif turn == '^':
        loc[1] += 1
    elif turn == 'v':
        loc[1] -= 1
    return loc 

def christmas(directions):
    current_loc = [[0, 0], [0, 0]]

    visit_map = defaultdict(lambda: 0)
    visit_map[(0, 0)] += 1

    for (santa, robot) in zip(directions[0::2], directions[1::2]):
        current_loc[0] = move(santa, current_loc[0])
        current_loc[1] = move(robot, current_loc[1])

        visit_map[tuple(current_loc[0])] += 1
        visit_map[tuple(current_loc[1])] += 1

    return len(visit_map)

print christmas(directions)
assert christmas('^v') == 3
assert christmas('^>v<') == 3
assert christmas('^v^v^v^v^v') == 11

