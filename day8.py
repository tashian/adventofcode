import re
import ast

code_len = 0
memory_len = 0
escaped_len = 0

with open('day8.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        code_len += len(line)
        evaluated_line = ast.literal_eval(line)
        memory_len += len(evaluated_line)
        escaped_line = re.escape(line)
        escaped_len += len(escaped_line) + 2
print memory_len, code_len, escaped_len
