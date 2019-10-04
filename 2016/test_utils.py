from utils import baseN, contains_two_distinct_letter_pairs, contains_isolated_repeated_letter, str_letter_groups

assert(baseN(57647112526) == 'hepxcrrq')
assert(list(str_letter_groups('abc', 1))) == [('a',), ('b',), ('c',)]
assert(list(str_letter_groups('abc', 2))) == [('a','b'), ('b','c')]
assert contains_two_distinct_letter_pairs('aabcdefgaa') == True
assert contains_two_distinct_letter_pairs('hello') == False
assert contains_two_distinct_letter_pairs('aaa') == False
assert contains_isolated_repeated_letter('xyx') == True
assert contains_isolated_repeated_letter('hello') == False
assert contains_isolated_repeated_letter('zz') == False
assert contains_isolated_repeated_letter('abcdefeghi') == True


