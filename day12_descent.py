import json
  
def descend(j):
    total = 0
    if type(j) is dict:
        j = j.values()
    for i in j:
        if type(i) is dict or type(i) is list:
            total += descend(i)
        elif type(i) is int:
            total += i
    return total

with open('day12.txt') as f:
    j = json.load(f)

print descend(j)
