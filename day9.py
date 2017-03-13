import re
import random
from itertools import permutations
from collections import defaultdict

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

def in_subset(subset, slot):
    return (1 << (slot - 1)) & subset

def subset_except(subset, slot):
    return subset ^ (1 << (slot - 1))

def dist(i, j):
    return edges[all_nodes[i], all_nodes[j]]

n = len(all_nodes)

A = [[float("inf") for i in xrange(n)] for j in xrange(2**n)]
# Base case
A[1][1] = 0

subsets = range(1, 2**n)
for subset in sorted(subsets, key=lambda x: bin(x).count('1')):
    if not in_subset(subset, 1):
        # City #1 is not presented.
        continue
    for i in xrange(2, n + 1):
        if not in_subset(subset, i):
            # City #j is not presented.
            continue
        for j in xrange(1, n + 1):
            if i == j or not in_subset(subset, j):
                continue
            print subset, i - 1, j - 1
            A[subset][i - 1] = \
                    min(A[subset][i - 1],
                        A[subset_except(subset, i)][j - 1] + dist(i - 1, j - 1))

print A
