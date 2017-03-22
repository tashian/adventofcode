import re

NUMBERS = re.compile('-?\d+')

assert(NUMBERS.findall('{"a":[-5,5,3],"b":-4}') == ['-5','5','3','-4'])

numbers = []
with open('day12.txt') as f:
    for line in f:
        numbers += NUMBERS.findall(line)

print sum(map(int, numbers))
