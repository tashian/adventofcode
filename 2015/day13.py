# Knights of the Dinner Table
# http://adventofcode.com/2015/day/13
# 
# - Everyone will have 2 neighbors (edges)
# - Weights of edges are positive or negative
# - Find the optimal seating arrangement and return
#   the total change in happiness of that arrangement.

import re
from collections import defaultdict
import itertools

def edges_for(arrangement):
    edges = zip(arrangement[0:], arrangement[1:])
    # Ensure sure the first and last people in the arrangement are counted as an edge
    edges.append((arrangement[-1], arrangement[0]))
    return edges

def day13(prefs):
    people = prefs.keys()
    optimal = 0
    for arrangement in itertools.permutations(people):
        happiness = 0
        for person1, person2 in edges_for(arrangement):
             happiness += prefs[person1][person2] + prefs[person2][person1]

        if happiness > optimal:
            optimal = happiness
    print optimal

LINE_FORMAT = re.compile(
    r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).'
)

prefs = defaultdict(dict)
with open('day13.txt') as f:
    for line in f:
        matches = LINE_FORMAT.match(line)
        n1, sign, points, n2 = matches.groups()
        points = int(points)
        if sign == 'lose':
            points *= -1
        prefs[n1][n2] = points

        # The next two lines solve part 2...
        prefs['Carl'][n1] = 0
        prefs[n1]['Carl'] = 0

if __name__ == '__main__':
    day13(prefs)
