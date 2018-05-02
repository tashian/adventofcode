batch = []
with open('day3.txt') as f:
    with open('day3_part2.txt', 'w') as out:
        for line in f:
            batch.append(line.split())
            if len(batch) == 3:
                batch = list(map(list, zip(*batch)))
                out.write('\n'.join([' '.join(i) for i in batch]))
                out.write('\n')
                batch = []

