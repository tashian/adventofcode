import regex

NUMBERS = regex.compile(r'-?\d+')
RED = regex.compile(r'\{(?>[^{]*:"red[^}]*|(?R))*\}')

numbers = []
with open('day12.txt') as f:
    for line in f:
        line = RED.sub('', line)
        numbers += NUMBERS.findall(line)

print sum([int(x) for x in numbers])
