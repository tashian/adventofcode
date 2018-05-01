# Medicine for Rudolph
# http://adventofcode.com/2015/day/19
from itertools import ifilter
import re

class FusionPlant(object):
    def __init__(self, reactions):
        self.reactions = reactions
	self.molecules = Molecules([r[0] for r in self.reactions])

    def replacements(self, starting_molecule):
        self.decompose_starting_molecule(starting_molecule)

	transformations = set()
	for i, (molecule, loc) in enumerate(self.molecules):
	    for reaction in self.reactions_for(molecule):
                transformations.add(self.transform(starting_molecule, loc, reaction))
	return transformations

    def reactions_for(self, molecule):
        for reaction in self.reactions:
            if reaction[0] == molecule:
                yield reaction

    def transform(self, starting_molecule, loc, reaction):
        return starting_molecule[0:loc] + reaction[1] + starting_molecule[loc+len(reaction[0]):]

    def decompose_starting_molecule(self, starting_molecule):
        # Break up starting molecule into a list of all single- and two-letter
        # values, in order, with their location in the starting molecule
        letters = list(starting_molecule)
	for i, letter in enumerate(letters):
	    self.molecules.add((letter, i))
            if i < len(letters) - 1:
                self.molecules.add((letters[i] + letters[i+1], i))

class Molecules(object):
    def __init__(self, reactants):
        self.reactants = reactants
        self.molecules = []

    def add(self, molecule):
        if molecule[0] in self.reactants:
            self.molecules.append(molecule)

    def __iter__(self):
        return iter(self.molecules)

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
                transformations = plant.replacements(line)
                print len(transformations)

