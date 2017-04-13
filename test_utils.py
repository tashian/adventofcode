from utils import baseN, contains_two_distinct_letter_pairs, contains_isolated_repeated_letter

assert(baseN(57647112526) == 'hepxcrrq')
assert contains_two_distinct_letter_pairs('aabcdefgaa') == True
assert contains_two_distinct_letter_pairs('hello') == False
assert contains_two_distinct_letter_pairs('aaa') == False
assert contains_isolated_repeated_letter('xyx') == True
assert contains_isolated_repeated_letter('hello') == False
assert contains_isolated_repeated_letter('zz') == False
assert contains_isolated_repeated_letter('abcdefeghi') == True

