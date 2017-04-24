# Day 23: Opening the Turing Lock
import re

src = []
INSTRUCTION=re.compile(r'(\w+) ([+\-\w\d]+)[, ]*([+\-\w\d]*)')
for line in open('day23.txt', 'r'):
    matches = INSTRUCTION.match(line.rstrip())
    src.append(tuple(i for i in matches.groups()))

pc = 0
regs = {'a': 0, 'b': 0}
while True:
    jump = 1
    command, param1, param2 = src[pc] 
    if command == 'hlf':
        regs[param1] //= 2
    elif command == 'tpl':
        regs[param1] *= 3
    elif command == 'inc':
        regs[param1] += 1
    elif command == 'jmp':
        jump = int(param1)
    elif command == 'jie':
        if regs[param1] % 2 == 0:
            jump = int(param2)
    elif command == 'jio':
        if regs[param1] == 1:
            jump = int(param2)
    else:
        print command, param1, param2
        raise ValueError
    pc += jump
    if pc >= len(src):
        break
print regs
