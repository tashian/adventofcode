import re

class LightGrid():
    def __init__(self):
        self.grid = self.emptyGrid()
        
    def emptyGrid(self):
        return [[False for k in xrange(1000)] for k in xrange(1000)]

    def turnOn(self, x1, y1, x2, y2):
        for i, j in self._gridRect(x1, y1, x2, y2):
            self.grid[i][j] = True

    def turnOff(self, x1, y1, x2, y2):
        for i, j in self._gridRect(x1, y1, x2, y2):
            self.grid[i][j] = False

    def toggle(self, x1, y1, x2, y2):
        for i, j in self._gridRect(x1, y1, x2, y2):
           self.grid[i][j] = not self.grid[i][j]

    def sum(self):
        return sum([self.grid[i].count(True) for i in xrange(0, 1000)])

    def _gridRect(self, x1 = 0, y1 = 0, x2 = 1000, y2 = 1000):
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                yield i, j 

myGrid = LightGrid()
lineMatcher = re.compile('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')
with open('day6.txt') as f:
    for i in f:
        print i
        match = lineMatcher.match(i)
        instruction = match.group(1)
        coords = map(int, match.groups()[1:])
        if instruction == 'toggle':
            myGrid.toggle(*coords)
        elif instruction == 'turn on':
            myGrid.turnOn(*coords)
        else:
            myGrid.turnOff(*coords)
        print myGrid.sum()
