# I want to store all of the instructions in a graph so that I can recurse through
# the network to evaluate a specific variable.
# 
# The first challenge is that I will "see" nodes before I understand how they connect
# with each other, so I have to make the whole map before I can evaluate anything.
#
# The second challenge is that recursive loops must be avoided, so I have to
# memoize each signal value once it is resolved.
#
import re
import abc

class Network(object):
    def __init__(self):
        self.values = {}

    def add(self, name, node):
        self.values[name] = node

    def evaluate(self, val):
        return self.values[val].evaluate()

class Node:
    __metaclass__ = abc.ABCMeta
    def __init__(self, net, left, right):
        self.signal = False
        self.net = net
        self.left = left
        self.right = right

    def evaluate(self):
        if not self.signal:
            self.signal = self._evaluate()
        return self.signal

    def _resolve(self, val):
        if type(val) is int:
            return val
        return self.net.evaluate(val)

    @abc.abstractmethod
    def _evaluate(self):
        pass

class AndNode(Node):
    def _evaluate(self):
        return self._resolve(self.left) & self._resolve(self.right)

class OrNode(Node):
    def _evaluate(self):
        return self._resolve(self.left) | self._resolve(self.right)

class NotNode(Node):
    def _evaluate(self):
        return (1 << 16) - 1 - self._resolve(self.right)

class LShiftNode(Node):
    def _evaluate(self):
        return self._resolve(self.left) << self.right

class RShiftNode(Node):
    def _evaluate(self):
        return self._resolve(self.left) >> self.right

class ValueNode(Node):
    def _evaluate(self):
        return self._resolve(self.left)

class Parser(object):
    OPCODES = {
        'NOT': NotNode,
        'OR': OrNode,
        'AND': AndNode,
        'LSHIFT': LShiftNode,
        'RSHIFT': RShiftNode,
        'NOT': NotNode
    }
    INSTRUCTION = re.compile('^(\w*)\s?(' + '|'.join(OPCODES.keys()) + ')\s(\w+)')

    def __init__(self, network):
        self.network = network

    def parse(self, line):
        instruction, destination = line.split(' -> ')
        matches = self.INSTRUCTION.match(instruction)
        if matches:
            self.add_instruction(destination, *matches.groups())
        else:
            self.add_assignment(destination, instruction)

    def add_instruction(self, destination, left, opcode, right):
        if left.isdigit():
            left = int(left)
        if right.isdigit():
            right = int(right)
        self.network.add(destination, self.OPCODES[opcode](self.network, left, right))

    def add_assignment(self, destination, instruction):
        if instruction.isdigit():
            instruction = int(instruction)
        self.network.add(destination, ValueNode(self.network, instruction, None))

network = Network()
parser = Parser(network)

with open('day7.txt') as f:
    for line in f:
        parser.parse(line.rstrip('\n'))

print network.evaluate('a')

# Rewiring for part two:
# network.values['b'] = ValueNode(network, 3176, None)

