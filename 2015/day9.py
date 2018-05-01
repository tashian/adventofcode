import re
import random
import itertools
import pprint
from collections import defaultdict

class UndirectedGraph:
    # edges are a dict in the form edges['A', 'B'] = 50,
    # where 50 is the distance between nodes A and B.
    def __init__(self, edges):
        self.edges = edges

    def distance(self, a, b):
        if self.edges[a, b]:
            return self.edges[a, b]
        return float("inf")

    def brute_force_tsp(self):
        all_nodes = set(sum(self.edges.keys(), ()))
        n = len(all_nodes)
        min_cost = float("inf")
        max_cost = 0
        for route in itertools.permutations(all_nodes):
            route_cost = 0
            for i in xrange(0, n-1):
                route_cost += self.distance(route[i], route[i+1])
            if route_cost < min_cost:
                min_cost, min_route = route_cost, route
            if route_cost > max_cost:
                max_cost, max_route = route_cost, route
        return Route(min_route, min_cost), Route(max_route, max_cost)

class Route:
    def __init__(self, route, cost):
        self.route = route
        self.cost = cost

    def pretty_print(self):
        pretty_route = ' -> '.join(self.route)
        pretty_route += '\nCost: ' + str(self.cost)
        print pretty_route

def run_from_input_file():
    edges = {}
    all_nodes = []
    with open('day9.txt') as f:
        route_re = re.compile('(\w+) to (\w+) = (\d+)')
        for line in f:
            matches = route_re.match(line)
            source, destination, distance = matches.groups()
            edges[source, destination] = int(distance)
            edges[destination, source] = int(distance)
    map(Route.pretty_print, UndirectedGraph(edges).brute_force_tsp())

run_from_input_file()
