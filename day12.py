import re

NUMBERS = re.compile('-?\d+')

assert(NUMBERS.findall('asd-5,5,3aksdjas-4') == ['-5','5','3','-4'])

numbers = []
with open('day12.txt') as f:
    for line in f:
        numbers += NUMBERS.findall(line)

print numbers
print sum(map(int, numbers))
