import re
import collections
from utils import list_of_lists, rotate_list

RotateRow = collections.namedtuple('RotateRow', ['row', 'distance'])
RotateColumn = collections.namedtuple('RotateColumn', ['column', 'distance'])
Rect = collections.namedtuple('Rect', ['xsize', 'ysize'])

def tokenize(data):
    TOKEN_SPEC = [
        ('RECT',   r'rect (\d+)x(\d+)'),
        ('ROTATE', r'rotate (row y|column x)=(\d+) by (\d+)'),
    ]
    TOKEN_REGEX = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    for mo in re.finditer(TOKEN_REGEX, data):
        kind = mo.lastgroup
        if kind == 'RECT':
            xsize = int(mo.group(2))
            ysize = int(mo.group(3))
            yield Rect(xsize, ysize)
        if kind == 'ROTATE':
            loc = int(mo.group(6))
            dist = int(mo.group(7))
            if mo.group(5) == 'row y':
                yield RotateRow(loc, dist)
            else:
                yield RotateColumn(loc, dist)


class Grid(object):
    def __init__(self):
        self.width = 50
        self.height = 6
        self.grid = list_of_lists(self.width, self.height, 0)

    def applyiter(self, iterator):
        for token in iterator:
            print(token)
            if type(token) == RotateRow:
                self.rotate_row(token.row, token.distance)
            if type(token) == RotateColumn:
                self.rotate_column(token.column, token.distance)
            if type(token) == Rect:
                self.rect(token.xsize, token.ysize)
            print(self)

    def __str__(self):
        s = ''
        for row in self.grid:
            s += ' '.join([str(col) for col in row]) + '\n'
        return s

    def rect(self, xsize, ysize):
        for x in range(xsize):
            for y in range(ysize):
                self.grid[y][x] = 1

    def rotate_row(self, i, dist):
        self.grid[i] = rotate_list(self.grid[i], dist)

    def rotate_column(self, i, dist):
        l = []
        for row in self.grid:
            l.append(row[i])
        l = rotate_list(l, dist)
        for j, row in enumerate(self.grid):
            row[i] = l[j]

    def lit(self):
        return sum([light for row in self.grid for light in row])

grid = Grid()
with open('day8.txt') as f:
    grid.applyiter(tokenize(f.read()))

print(grid.lit())

