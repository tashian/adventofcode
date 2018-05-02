from collections import defaultdict
import re

def most_common_letters(s):
    counts = defaultdict(int)
    for i in list(s):
        if i != '-':
            counts[i] += 1 
    l = sorted(counts.iteritems(), key=lambda (k,v): (v,k))
    l = sorted(l, key=lambda i: i[1], reverse=True)
    return ''.join([i[0] for i in l[:5]])

assert(most_common_letters("aaaaa-bbb-z-y-x") == "abxyz")
assert(most_common_letters("a-b-c-d-ee-f-g-h") == "eabcd")
assert(most_common_letters("aaa") == "a")

def decode(s):
    LINE = re.compile('([a-z+\-]*)-(\d+)\[(\w+)]')
    return list(LINE.match(s).groups())

with open('day4.txt') as f:
    i = 0
    for line in f:
        encrypted, sid, checksum = decode(line)
        if most_common_letters(encrypted) == checksum:
            i += int(sid)
    print(i)
        

