valids = 0
with open('day3_part2.txt') as f:
    for line in f:
        sides = [int(l) for l in line.split()]
        if sides[0] + sides[1] > sides[2] \
        and sides[0] + sides[2] > sides[1] \
        and sides[1] + sides[2] > sides[0]:
            valids += 1

print(valids)
