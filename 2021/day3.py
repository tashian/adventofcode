with open('day3.txt') as f:
    data = f.read().split()

pivoted = [[] for x in range(len(data[0]))]
for line in data:
  for c, ch in enumerate(list(line)):
    pivoted[c].append(ch)

def most_common(lst):
  return max(set(lst), key=lst.count)

def binary_complement(b):
  length = len(b)
  i = int(b, 2)
  return int(format(~i & int('1' * length, 2), 'b'), 2)

gamma = ''
for p in pivoted:
  gamma = gamma + most_common(p)

epsilon = binary_complement(gamma)
gamma = int(gamma, 2)

print(gamma)
print(epsilon)

