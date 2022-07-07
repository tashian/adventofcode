import copy

with open('day3.txt') as f:
    data = f.read().split()

def most_common_bit(l):
  if l.count('1') >= l.count('0'):
      return '1'
  else:
      return '0'

def least_common_bit(l):
  if l.count('0') <= l.count('1'):
      return '0'
  else:
      return '1'

def frequency_bit(data, position, fn):
    column = []
    for line in data:
        column.append(line[position])

    return fn(column)

o2_lines = copy.deepcopy(data)
co2_lines = copy.deepcopy(data)
bitlength = len(data[0])
for position in range(bitlength):
   most = frequency_bit(o2_lines, position, most_common_bit)
   least = frequency_bit(co2_lines, position, least_common_bit)

   if len(o2_lines) > 1:
       o2_lines = [line for line in o2_lines if line[pos] == most]
   if len(co2_lines) > 1:
       co2_lines = [line for line in co2_lines if line[pos] == least]

print(int(o2_lines[0], 2) * int(co2_lines[0], 2))
