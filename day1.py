def count_floors(directions):
    result = 0
    for i, dir in enumerate(list(directions)):
        if dir == '(':
            result += 1
        elif dir == ')':
            result -= 1
        if result == -1:
            print "basement at position ", i+1
    return result


assert count_floors('()()') == 0
assert count_floors('))(((((') == 3
assert count_floors(')())())') == -3

i = open('day1.txt', 'r')
directions = i.read()
print len(directions)
print count_floors(directions)
