from collections import defaultdict

with open('day3.txt', 'r') as day3:
    directions = day3.read()

visit_map = defaultdict(lambda: 0)
x, y = 0, 0

def move(turn):
    global x, y
    if turn == '>':
        x += 1
    elif turn == '<':
        x -= 1
    elif turn == '^':
        y += 1
    elif turn == 'v':
        y -= 1

visit_map[(x, y)] += 1
for turn in directions:
    move(turn)
    visit_map[(x, y)] += 1

print len(visit_map)
