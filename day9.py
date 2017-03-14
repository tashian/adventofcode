# Depends on LKH TSP solver binary from http://www.akira.ruc.dk/~keld/research/LKH/
# And on the pytsp package

# Run this script as:
#   LKH=path_to_LKH_binary python day9.py

import re
import random
import itertools
import pprint
from collections import defaultdict

def infinity():
    return float("inf")

edges = defaultdict(infinity)
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

n = len(all_nodes)

mincost = float("inf")
maxcost = 0
n = len(all_nodes)
for route in itertools.permutations(all_nodes):
    routecost = 0
    for i in range(0, n-1):
        routecost += edges[route[i], route[i+1]]
    if routecost < mincost:
        mincost = routecost
        minroute = route
    if routecost > maxcost:
        maxcost = routecost
        maxroute = route

def pretty_route(route):
    pretty_route = ""
    for i in range(0, n-1):
        pretty_route += '  {} -> {} = {}\n'.format(route[i], route[i+1], edges[route[i], route[i+1]])
    return pretty_route

print "Shortest route:"
print pretty_route(minroute)

print "Longest route:"
print pretty_route(maxroute)

print "Min cost:", mincost, "max cost:", maxcost

