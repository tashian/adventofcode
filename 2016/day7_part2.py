import re
from utils import str_letter_groups

SEGMENTS = re.compile(r"""([^\[\]]*)\[([^\]]+)\]([^\[\]]*)""")

with open('day7.txt') as f:
    addresses = f.read().split()

def is_ssl(addr):
    hypernets = []
    supernets = []
    for mg in SEGMENTS.findall(addr):
        supernets.append(mg[0])
        supernets.append(mg[2])
        hypernets.append(mg[1])
    if aba_bab(hypernets, supernets):
       return True
    return False

def aba_bab(hypernets, supernets):
    def is_aba(s):
        if s[0] == s[2] and s[0] != s[1]:
            return True
        return False

    def is_inverse_of(s1, s2):
        if s1[0] == s2[1] == s1[2] and s1[1] == s2[0] == s2[2]:
            return True
        return False

    def all_letter_triplets(l):
        return [i for sublist in [str_letter_groups(s, 3) for s in l] for i in sublist]

    for g in all_letter_triplets(hypernets):
        for h in all_letter_triplets(supernets):
            if is_aba(g) and is_aba(h) and is_inverse_of(g, h):
                return True
    return False


print(is_ssl('aba[bab]xyz')) # true
print(is_ssl('xyx[xyx]xyx')) # false
print(is_ssl('aaa[kek]eke')) # true
print(is_ssl('zazbz[bzb]cdb')) # true
print(len(list(filter(is_ssl, addresses))))

