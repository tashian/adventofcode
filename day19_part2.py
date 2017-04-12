# Medicine for Rudolph, Part 2
# 
# http://adventofcode.com/2015/day/19
#
# My plan for this is to reduce the starting molecule down to "e" by looping
# through all possible reactions starting from the longest product
# and moving toward the shortest, looking for opportunities to reduce the total
# length of the molecule the most with each reduction.
#
import utils
import re

def main():
    LINE_FORMAT = re.compile(r'(\w+) => (\w+)')
    reactions_by_product = {}
    with open('day19.txt') as f:
        for line in f:
            matches = LINE_FORMAT.match(line)
            if matches:
                reactions_by_product[matches.group(2)] = matches.group(1)
            elif len(line) > 1:
                starting_molecule = line
    print len(reactions_by_product), 'available reactions'

    repeating = True
    replacements = 0
    while repeating:
        repeating = False
        for product in sorted(reactions_by_product.keys(), key=lambda x: len(x), reverse=True):
            while product in starting_molecule:
                print "replacing", product, "with", reactions_by_product[product]
                repeating = True
                loc = starting_molecule.find(product)
                replacements += 1
                starting_molecule = utils.string_replace(
                    starting_molecule,
                    loc,
                    loc + len(product),
                    reactions_by_product[product]
                )
            if repeating:
                break
    print replacements, "replacements"

if __name__ == '__main__':
    main()

