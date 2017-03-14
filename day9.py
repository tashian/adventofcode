import re
import random
import itertools

edges = {}
all_nodes = []
route_re = re.compile('(\w+) to (\w+) = (\d+)')
with open('day9.txt') as f:
    for line in f:
        matches = route_re.match(line)
        source, destination, distance = matches.groups()
        if source not in all_nodes:
            all_nodes.append(source)
        if destination not in all_nodes:
            all_nodes.append(destination)
        edges[source, destination] = int(distance)
        edges[destination, source] = int(distance)

def distance(i, j):
    if (all_nodes[i], all_nodes[j]) in edges:
        return edges[all_nodes[i], all_nodes[j]]
    else:
        return float("inf")

def solve_tsp_dynamic(points, distf):
    # calc all lengths
    n = len(points)
    all_distances = [[distf(x,y) for y in xrange(n)] for x in xrange(n)]
    # initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx, dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
                print m, S, j
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]

path = solve_tsp_dynamic(all_nodes, distance)
route = map(lambda x: all_nodes[x], path)
print route
prev_point = None

cost = 0
for i, point in enumerate(route):
    if i == 0:
        prev_point = point
        continue
    cost += edges[prev_point, point]
    prev_point = point
print cost

