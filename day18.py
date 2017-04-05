import unittest
import copy

# Like a GIF for your yard
# Rules: 
# Max 100x100 square grid of lights
# '#' is on, '.' is off
# A light stays on if 2-3 neighbors are on
# A light turns on if exactly 3 neighbors are on

class Grid():
    def __init__(self, grid):
        self.grid = grid

    def litCount(self):
        return sum([sum(line) for line in self.grid])

    def step(self):
        newGrid = copy.deepcopy(self.grid)
        for i, line in enumerate(self.grid):
            for j, light in enumerate(line):
                neighbors = [
                    self.testNeighbor(i-1, j-1),
                    self.testNeighbor(i-1, j),
                    self.testNeighbor(i-1, j+1),
                    self.testNeighbor(i, j-1),
                    self.testNeighbor(i, j+1),
                    self.testNeighbor(i+1, j-1),
                    self.testNeighbor(i+1, j),
                    self.testNeighbor(i+1, j+1)
                ]
                litNeighbors = sum(neighbors)
                if litNeighbors < 2 or litNeighbors > 3:
                    newGrid[i][j] = 0
                if litNeighbors == 3:
                    newGrid[i][j] = 1
        self.grid = newGrid

    def testNeighbor(self, i, j):
        if i < 0 or j < 0:
            return False
        try:
            if self.grid[i][j] == 1:
                return True
            else:
                return False
        except IndexError:
            return False

class GridPrinter():
    def __init__(self, grid):
        self.grid = grid.grid

    def pretty_print(self):
        print ''.join(['.' if i == 0 else '#' if i == 1 else i
                for i in reduce(lambda a, b: a + ['\n'] + b, self.grid)])

class GridReader():
    def __init__(self, grid):
        self.grid = [[0 if c == '.' else 1 for c in list(line)]
                    for line in grid]

if __name__ == '__main__':
    with open('day18.txt') as f:
        grid = Grid(GridReader([line.rstrip() for line in f]).grid)
        for i in range(0,100):
            grid.step()
        print grid.litCount()
