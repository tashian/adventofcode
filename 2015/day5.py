class SantaString:
    EVIL_LETTERS = ["ab", "cd", "pq", "xy"]
    VOWELS = ['a','e','i','o','u']

    def __init__(self, s = ''):
        self.s = s

    def setValue(self, s):
        self.s = s
        return self

    def nice(self):
        if not self.contains_at_least_three_vowels():
            return False
        if not self.contains_double_letter():
            return False
        if self.contains_evil_letters():
            return False
        return True

    def contains_double_letter(self):
        for i, letter in enumerate(self.s):
            if i == 0:
                next
            if self.s[i-1] == letter:
                return True
        return False

    def contains_evil_letters(self):
        for i in xrange(len(self.EVIL_LETTERS)):
            if self.EVIL_LETTERS[i] in self.s:
                return True
        return False

    def contains_at_least_three_vowels(self):
        vowel_count = 0
        for letter in self.s:
            for vowel in self.VOWELS:
                if letter == vowel:
                    vowel_count += 1
        if vowel_count >= 3:
            return True
        return False

assert SantaString('ugknbfddgicrmopn').nice() == True
assert SantaString('aaa').nice() == True
assert SantaString('jchzalrnumimnmhp').nice() == False
assert SantaString('haegwjzuvuyypxyu').nice() == False
assert SantaString('dvszwmarrgswjxmb').nice() == False

ss = SantaString()
with open('day5.txt') as f:
    print sum([ss.setValue(s).nice() for s in f])

