import re

SEGMENTS = re.compile(r"""([^\[\]]*)\[([^\]]+)\]([^\[\]]*)""")
ABBA = re.compile(r"""(\w)(\w)(?<!\1)\2\1""")

with open('day7.txt') as f:
    addresses = f.read().split()

def is_tls(addr):
    outer = inner = ''
    for mg in SEGMENTS.findall(addr):
        outer += mg[0] + ' ' + mg[2]
        inner += mg[1] + ' '
    if ABBA.search(outer) is not None and ABBA.search(inner) is None:
       return True
    return False

print(is_tls('abba[mnop]qrst'))
print(is_tls('abcd[bddb]xyyx'))
print(is_tls('aaaa[qwer]tycbui'))
print(is_tls('ioxxoj[asdfgh]zxcvbn'))
print(is_tls('pgraswoweceiftu[khhpmbjghxgmhsud]axqjkekmecwunefk[pvelpeorryjcstk]lruensapttjtyxnr'))
print(len(list(filter(is_tls, addresses))))

