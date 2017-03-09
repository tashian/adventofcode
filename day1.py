def count_floors(directions):
    result = 0
    for dir in list(directions):
        if dir == '(':
            result += 1
        elif dir == ')':
            result -= 1
    return result

print count_floors(directions)

assert count_floors('()()') == 0
assert count_floors('))(((((') == 3
assert count_floors(')())())') == -3

i = open('day1.txt', 'r')
directions = i.read()
print len(directions)

