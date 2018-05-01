import json
  
def descend(j):
    total = 0
    check_red = False
    if type(j) == dict:
        j = j.values()
        check_red = True
    for i in j:
        if check_red and type(i) is unicode and i == "red":
            return 0
        if type(i) is dict or type(i) is list:
            total += descend(i)
        elif type(i) is int:
            total += i
    return total

with open('day12.txt') as f:
    j = json.load(f)

print descend(j)
