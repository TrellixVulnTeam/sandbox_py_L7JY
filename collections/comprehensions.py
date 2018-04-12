# 内包表記

nums = range(3, 21)
halves = []
for num in nums:
    halves.append(num / 2)
print(halves)

halves = [num / 2 for num in nums]
print(halves)

print('---')
print([num for num in range(1, 101) if num % 3 == 0])

print('---')
print([(x, x**2) for x in range(11)])

print('---')
from math import pi
print([round(pi, i) for i in range(11)])

print('---')
print({x: x**2 for x in range(11)})

print('---')
print({x for x in 'superduper' if x not in 'pd'})

print('---')
rows = range(4)
cols = range(10)
print([(col, row) for row in rows for col in cols])

print('---')
print({number: letter for letter, number
       in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))})

print('---')
