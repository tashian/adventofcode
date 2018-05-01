# Same rules as day18, but this time the corner
# lights are stuck on.

from day18 import Grid, Light, main
import copy

class StuckGrid(Grid):
    FOUR_CORNERS = [[0,0], [-1,-1], [0,-1], [-1,0]]

    def __init__(self, grid):
        self.grid = grid
        for i, j in self.FOUR_CORNERS:
            self.grid[i][j] = StuckLight(True)

class StuckLight(Light):
    def update(self, litNeighbors):
	return self.status

if __name__ == '__main__':
    main(StuckGrid)
