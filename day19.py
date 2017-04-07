# Medicine for Rudolph
# http://adventofcode.com/2015/day/19
from itertools import ifilter
import re

class FusionPlant(object):
    def __init__(self, reactions):
        self.reactions = reactions

    def all_possible_molecules(self, starting_molecule):
	molecules = self.deconstruct_starting_molecule(starting_molecule)

	# Put all transformations into a set
	transformations = set()
	for i, (molecule, loc) in enumerate(molecules):
	    for reaction in self.reactions:
		if reaction[0] == molecule:
                    transformed_molecule = starting_molecule[0:loc] + reaction[1] + starting_molecule[loc+len(molecule):]
		    transformations.add(transformed_molecule)
	return transformations

    def deconstruct_starting_molecule(self, starting_molecule):
        # Break up starting molecule into a list of all single- and two-letter
        # values, in order
        letters = list(starting_molecule)
	molecules = []
	for i, letter in enumerate(letters):
	    molecules.append((letter, i))
	    if i < len(letters)-1:
	        molecules.append((letters[i] + letters[i+1], i))

        # Filter based on the reactions available
	reactants = [x[0] for x in self.reactions]
        molecules = list(ifilter(lambda z: z[0] in reactants, molecules))
	return molecules

if __name__ == '__main__':
    LINE_FORMAT = re.compile(r'(\w+) => (\w+)')
    reactions = []
    with open('day19.txt') as f:
        for line in f:
            matches = LINE_FORMAT.match(line)
            if matches:
                reactions.append(matches.groups())
            elif len(line) > 1:
                plant = FusionPlant(reactions)
                transformations = plant.all_possible_molecules(line)
                print len(transformations)

