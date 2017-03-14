# Depends on LKH TSP solver binary from http://www.akira.ruc.dk/~keld/research/LKH/
# And on the pytsp package

# Run this script as:
#   LKH=path_to_LKH_binary python day9.py

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
        return 0


n = len(all_nodes)
matrix = [[distance(i, j) for i in xrange(n)] for j in xrange(n)]

print all_nodes
print matrix

from pytsp import atsp_tsp, run, dumps_matrix

matrix_sym = atsp_tsp(matrix, strategy="avg")

outf = "/tmp/myroute.tsp"
with open(outf, 'w') as dest:
    dest.write(dumps_matrix(matrix_sym, name="My Route"))

# tour = run(outf, start=10, solver="concorde")
# print tour

