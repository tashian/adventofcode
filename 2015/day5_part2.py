import utils

def nice(s):
    if not utils.contains_two_distinct_letter_pairs(s):
        return False
    if not utils.contains_isolated_repeated_letter(s):
        return False
    return True

assert nice('qjhvhtzxzqqjkmpb') == True
assert nice('xxyxx') == True
assert nice('uurcxstgmygtbstg') == False
assert nice('ieodomkazucvgmuy') == False

with open('day5.txt') as f:
    print sum([nice(s) for s in f])
