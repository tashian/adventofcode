import unittest
from day18 import Grid, GridReader

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

    def test_after_one_step(self):
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

    def test_after_two_steps(self):
        # After 2 steps:
        # ..###.
        # ......
        # ..###.
        # ......
        # .#....
        # .#....
        grid = Grid(TestGrid.INPUT)
        grid.step()
        grid.step()
        self.assertEqual(grid.litCount(), 8)

if __name__ == '__main__':
    unittest.main()

