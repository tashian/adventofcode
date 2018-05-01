import unittest
from day18 import Grid, GridReader, GridPrinter
from day18_part2 import StuckGrid

class TestGrid(unittest.TestCase):
    INPUT = GridReader(
            ['.#.#.#',
             '...##.',
             '#....#',
             '..#...',
             '#.#..#',
             '####..']).grid
    
    def test_initial_state(self):
        grid = Grid(TestGrid.INPUT)
        self.assertEqual(grid.litCount(), 15)

    def test_after_steps(self):
        grid = Grid(TestGrid.INPUT)
        grid.step()
        # After 1 step:
        # ..##..
        # ..##.#
        # ...##.
        # ......
        # #.....
        # #.##..
        self.assertEqual(grid.litCount(), 11)
        grid.step()
        # After 2 steps:
        # ..###.
        # ......
        # ..###.
        # ......
        # .#....
        # .#....
        self.assertEqual(grid.litCount(), 8)

class TestStuckGrid(unittest.TestCase):
    def test_initial_state(self):
        grid = StuckGrid(TestGrid.INPUT)
        self.assertEqual(grid.litCount(), 17)

    def test_after_steps(self):
        grid = StuckGrid(TestGrid.INPUT)
	grid.step()
	# After 1 step:
	# #.##.#
	# ####.#
	# ...##.
	# ......
	# #...#.
	# #.####
	self.assertEqual(grid.litCount(), 18)
	grid.step()
	# After 2 steps:
	# #..#.#
	# #....#
	# .#.##.
	# ...##.
	# .#..##
	# ##.###
	self.assertEqual(grid.litCount(), 18)

if __name__ == '__main__':
    unittest.main()

