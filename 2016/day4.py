from collections import Counter
import re

def checksum(s):
    counts = Counter(s)
    del counts['-']
    l = sorted(counts.items(), key=lambda v: (v[0],v[1]))
    l = sorted(l, key=lambda i: i[1], reverse=True)
    return ''.join([i[0] for i in l[:5]])

assert(checksum("aaaaa-bbb-z-y-x") == "abxyz")
assert(checksum("a-b-c-d-ee-f-g-h") == "eabcd")
assert(checksum("aaa") == "a")

def decode(s):
    LINE = re.compile('([a-z+\-]*)-(\d+)\[(\w+)]')
    return list(LINE.match(s).groups())

with open('day4.txt') as f:
    i = 0
    for line in f:
        encrypted, sid, check = decode(line)
        if checksum(encrypted) == check:
            i += int(sid)
    print(i)
