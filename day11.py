import unittest
import re

def next_password(n):
    while True:
        pw = baseN(n)
        n += 1
        if contains_restricted_letters(pw):
            continue
        if not contains_straight(pw):
            continue
        if not contains_pairs(pw):
            continue
        break
    return pw

def contains_restricted_letters(pw):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return True
    return False

def contains_straight(pw):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for triplets in zip(alphabet[0::1], alphabet[1::1], alphabet[2::1]):
        if ''.join(triplets) in pw:
            return True
    return False

PAIRS = re.compile(r'(.)\1')
def contains_pairs(pw):
    if len(PAIRS.findall(pw)) >= 2:
        return True
    return False

def baseN(num, b = 26, numerals = "abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

class TestCorporatePolicy(unittest.TestCase):
    def test_contains_straight(self):
        self.assertEqual(contains_straight('aabc'), True)
        self.assertEqual(contains_straight('anrkfbca', False)

    def test_contains_pairs(self):
        self.assertEqual(contains_pairs('aabb'), True)
        self.assertEqual(contains_pairs('daakrccj'), True)
        self.assertEqual(contains_pairs('aaakrzzj'), True)

    def test_baseN(self):
        self.assertEqual(baseN(57647112526), 'hepxcrrq')

# print next_password(57647112526)
# print next_password(57647486572)

if __name__ == '__main__':
    unittest.main()
