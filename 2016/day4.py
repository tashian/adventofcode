from collections import Counter
import re

def checksum(s):
    counts = Counter(s)
    del counts['-']

    # top-level sort by descending occurance counts, subsort by letters
    l = sorted(counts.most_common(), key=lambda v: (-v[1], v[0]))

    return ''.join([i[0] for i in l[:5]])

def decode(s):
    LINE = re.compile('([a-z+\-]*)-(\d+)\[(\w+)]')
    return list(LINE.match(s).groups())

if __name__ == "__main__":
    assert(checksum("aaaaa-bbb-z-y-x") == "abxyz")
    assert(checksum("a-b-c-d-ee-f-g-h") == "eabcd")
    assert(checksum("aaa") == "a")

    with open('day4.txt') as f:
        i = 0
        for line in f:
            encrypted, sid, check = decode(line)
            if checksum(encrypted) == check:
                i += int(sid)
        print(i)
