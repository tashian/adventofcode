def contains_two_distinct_letter_pairs(s):
    for i, couplet in enumerate(zip(s[0::1], s[1::1])):
        if i == len(s)-2:
            return False
        for j in range(i+2, len(s)-1):
            if (s[j], s[j+1]) == couplet:
                return True

def contains_isolated_repeated_letter(s):
    if len(s) == 2:
        return False
    for i, letter in enumerate(s):
        if s[i+2] == letter:
            return True
        if i+2 == len(s)-1:
            break
    return False

def nice(s):
    if not contains_two_distinct_letter_pairs(s):
        return False
    if not contains_isolated_repeated_letter(s):
        return False
    return True

assert contains_two_distinct_letter_pairs('aabcdefgaa') == True
assert contains_two_distinct_letter_pairs('hello') == False
assert contains_two_distinct_letter_pairs('aaa') == False
assert contains_isolated_repeated_letter('xyx') == True
assert contains_isolated_repeated_letter('hello') == False
assert contains_isolated_repeated_letter('zz') == False
assert contains_isolated_repeated_letter('abcdefeghi') == True
assert nice('qjhvhtzxzqqjkmpb') == True
assert nice('xxyxx') == True
assert nice('uurcxstgmygtbstg') == False
assert nice('ieodomkazucvgmuy') == False

with open('day5.txt') as f:
    print sum([nice(s) for s in f])
