# Medicine for Rudolph, Part 2
# 
# http://adventofcode.com/2015/day/19
#
# My plan for this is to reduce the starting molecule down to "e" by looping
# through all possible reactions starting from the longest resultant molecule
# and moving toward the shortest, looking for opportunities to reduce the total
# length of the molecule the most with each reduction.
#
from itertools import ifilter
import re

def main():
    LINE_FORMAT = re.compile(r'(\w+) => (\w+)')
    reactions = {}
    with open('day19.txt') as f:
        for line in f:
            matches = LINE_FORMAT.match(line)
            if matches:
                reactions[matches.group(2)] = matches.group(1)
            elif len(line) > 1:
                starting_molecule = line
    print len(reactions), 'available reactions'

    repeating = True
    replacements = 0
    while repeating:
        repeating = False
        for resulting_molecule in sorted(reactions.keys(), key=lambda x: 0-len(x)):
            while resulting_molecule in starting_molecule:
                print "replacing", resulting_molecule, "with", reactions[resulting_molecule]
                repeating = True
                loc = starting_molecule.find(resulting_molecule)
                replacements += 1
                starting_molecule = string_replace(
                    starting_molecule,
                    loc,
                    loc + len(resulting_molecule),
                    reactions[resulting_molecule]
                )
            if repeating:
                break
    print replacements, "replacements"

# This does the actual transformation and returns the result
def string_replace(s, start, end, replace_with):
    return s[0:start] + replace_with + s[end:]

if __name__ == '__main__':
    main()

