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
        return sum([sum(l.status for l in line) for line in self.grid])

    def step(self):
        grid = self._gridCopyForStep()
        for i, line in enumerate(self.grid):
            for j, _ in enumerate(line):
                grid[i][j].update(self.litNeighborCount(i, j))
        self.grid = grid

    def _gridCopyForStep(self):
        return copy.deepcopy(self.grid)

    def litNeighborCount(self, i, j):
        return sum([
	    self.neighborStatus(i-1, j-1),
	    self.neighborStatus(i-1, j),
	    self.neighborStatus(i-1, j+1),
	    self.neighborStatus(i, j-1),
	    self.neighborStatus(i, j+1),
	    self.neighborStatus(i+1, j-1),
	    self.neighborStatus(i+1, j),
	    self.neighborStatus(i+1, j+1)
	])

    def neighborStatus(self, i, j):
        if i < 0 or j < 0:
            return False
        try:
            return self.grid[i][j].status
        except IndexError:
            return False

class Light():
    def __init__(self, status):
	self.status = status

    def update(self, litNeighbors):
        if litNeighbors < 2 or litNeighbors > 3:
            self.status = False
        if litNeighbors == 3:
            self.status = True
        return self.status

class GridPrinter():
    def __init__(self, grid):
        self.grid = grid.grid

    def pretty_print(self):
        print ''.join(['.' if i == False else '#' if i == True else i
                for i in self.flattened_grid_with_newlines()])

    def flattened_grid_with_newlines(self):
	return reduce(lambda a, b: a + ['\n'] + b, self.grid)

class GridReader():
    def __init__(self, grid):
        self.grid = [[Light(False) if c == '.' else Light(True) for i, c in enumerate(list(line))]
                    for j, line in enumerate(grid)]

def main(gridclass):
    with open('day18.txt') as f:
        grid = gridclass(GridReader([line.rstrip() for line in f]).grid)
        for i in range(0,100):
            grid.step()
        print grid.litCount()

if __name__ == '__main__':
    main(Grid)
