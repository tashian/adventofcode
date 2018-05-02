from collections import Counter
import re

def checksum(s):
    # s = "bhha"
    counts = Counter(s)
    del counts['-']
    # counts = {'h': 2, 'b': 1, 'a': 1}

    # subsort by letters
    l = sorted(counts.items(), key=lambda v: (v[0],v[1]))
    # l = [('a', 1), ('b', 1), ('h', 2)]

    # top-level sort by descending occurance counts
    l = sorted(l, key=lambda i: i[1], reverse=True)
    # l = [('h', 2), ('a', 1), ('b', 1)]

    return ''.join([i[0] for i in l[:5]])

assert(checksum("aaaaa-bbb-z-y-x") == "abxyz")
assert(checksum("a-b-c-d-ee-f-g-h") == "eabcd")

def decode(s):
    LINE = re.compile('([a-z+\-]*)-(\d+)\[(\w+)]')
    return list(LINE.match(s).groups())

def rot(s, times):
    return ''.join([rot_ch(ch, times) for ch in list(s)])

def rot_ch(ch, times):
    if ch == '-':
        return ' '
    i = ord(ch) + (times % 26)
    if i > 122:
        i = (i - 123) + 97
    return chr(i)

assert(rot("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name")

with open('day4.txt') as f:
    i = 0
    for line in f:
        encrypted, sid, check = decode(line)
        if checksum(encrypted) == check:
            if rot(encrypted, int(sid)).endswith('storage'):
                print(sid, rot(encrypted, int(sid)))
