# Convert a number to a different base (default base 26)
def baseN(num, b = 26, numerals = "abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def list_of_lists(rows, cols, zerovalue=None):
    return [[zerovalue for k in range(rows)] for k in range(cols)]

def rotate_list(l, d=1):
   if len(l) == 0 or d == 0:
      return l
   d = -d % len(l)     # flip rotation direction
   return l[d:] + l[:d]


# Fast factoring via http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# This does the actual transformation and returns the result
def string_replace(s, start, end, replace_with):
    return s[0:start] + replace_with + s[end:]

def str_letter_groups(s, size):
    return zip(*[s[i:] for i in range(size)])

def contains_two_distinct_letter_pairs(s):
    for i, couplet in enumerate(str_letter_groups(s, 2)):
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

