from collections import Counter, defaultdict

with open('day6.txt') as f:
    signal = f.read()

words = signal.split()
print(len(words), "words")

most_common = ''
least_common = ''

# Rotate
for i in range(8):
    letters = []
    for word in words:
        letters.append(word[i])

    most_common += Counter(letters).most_common(1)[0][0]
    least_common += Counter(letters).most_common()[:0:-1][0][0]

print(most_common, least_common)

