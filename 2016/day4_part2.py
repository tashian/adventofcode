from collections import Counter
import re
from day4 import checksum, decode

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
