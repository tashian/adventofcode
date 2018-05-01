# Aunt Sue
# http://adventofcode.com/2015/day/16
# 

TARGET_COMPOUNDS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def day16(sues):
    for sue in sues:
        matches = 0
        for compound in sues[sue]:
            if comparitor(compound[0], compound[1]):
                matches += 1
        if matches == 3:
            print sue

def comparitor(compound, reading):
    target = TARGET_COMPOUNDS[compound]
    if compound == 'cats' or compound == 'trees':
        return target < reading
    if compound == 'pomeranians' or compound == 'goldfish':
        return target > reading
    return target == reading

import regex

LINE_FORMAT = regex.compile(
        r'Sue (?P<sue>\d+): (?:(?P<compound>\w+): (?P<amount>\d+)[, ]*)+'
)

with open('day16.txt') as f:
    sues = {}
    for line in f:
        matches = LINE_FORMAT.match(line)
        values = matches.capturesdict()
        sues[int(values['sue'][0])] = zip(values['compound'], map(int, values['amount']))
    day16(sues)
