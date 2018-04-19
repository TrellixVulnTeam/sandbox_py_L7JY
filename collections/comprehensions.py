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
print([(x, x ** 2) for x in range(11)])

print('---')
from math import pi

print([round(pi, i) for i in range(11)])

print('---')
print({x: x ** 2 for x in range(11)})

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
total_nums = range(1, 101)
fizzbuzzes = {
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz': [n for n in total_nums if n % 7 == 0]
}
print(fizzbuzzes)

print('---')
print({round(x / y) for y in range(1, 11) for x in range(2, 21)})
print([round(x / y) for y in range(1, 11) for x in range(2, 21)])

print('---')
fizzbuzzes2 = {key: set(value) for key, value in fizzbuzzes.items()}
print(fizzbuzzes2)

# fizzbuzzes2['fizzbuzz'] = {n for n in fizzbuzzes2['fizz'].intersection(fizzbuzzes2['buzz'])}
fizzbuzzes2['fizzbuzz'] = {n for n in fizzbuzzes2['fizz'] & fizzbuzzes2['buzz']}
print(fizzbuzzes2['fizzbuzz'])
