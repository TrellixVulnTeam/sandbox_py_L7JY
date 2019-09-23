"""
Comprehension（内包表記）
ref: Functional Programming, Generators
"""
import random

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
print(', '.join(str(x) for x in [4, 3, 6]))

print('---')
total_nums = range(1, 101)
fizzbuzzes = {
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz': [n for n in total_nums if n % 7 == 0]
}
print(fizzbuzzes)

print('---')
print([round(x / y) for y in range(1, 11) for x in range(2, 21)])

print('---')
fizzbuzzes2 = {key: set(value) for key, value in fizzbuzzes.items()}
print(fizzbuzzes2)

# fizzbuzzes2['fizzbuzz'] = {n for n in fizzbuzzes2['fizz'].intersection(fizzbuzzes2['buzz'])}
fizzbuzzes2['fizzbuzz'] = {
    n for n in fizzbuzzes2['fizz'] & fizzbuzzes2['buzz']}
print(fizzbuzzes2['fizzbuzz'])

print('--- list ---')
letters = [chr(code) for code in range(ord('a'), ord('z'))]
print(letters)
random_letters = [random.choice(letters) for _ in range(100)]
print(random_letters)

print('---')
import functools

cart = [
    ['Coffee', 7.99, 2],
    ['Bread', 2.99, 1],
    ['Apple', 0.99, 2],
    ['Milk', 4.99, 1],
    ['Cola', 1.99, 4],
]
sales_tax = 0.07

cart_item_totals = [item_name + ' ' + str(item_price * item_qty)
                    for (item_name, item_price, item_qty) in cart]
print(cart_item_totals)

# 2,3列目を掛けて合計
cart_subtotal = functools.reduce(lambda x, y: x + y[0] * y[1], [item[1:] for item in cart], 0)
print(cart_subtotal)

item_prices_plus_tax = [round(price * (1 + sales_tax), 2)
                        for price in [item[1] for item in cart]]
print(item_prices_plus_tax)

print('--- predicate ---')
cart_items_one_count = [item for item in cart if item[2] == 1]
print(cart_items_one_count)
cart_items_one_count_2 = ['{}: {} * {}'.format(name, price, qty)
                          for (name, price, qty) in cart if qty == 1]
print(cart_items_one_count_2)

print('--- generator ---')
gen_squares = (x * x for x in range(1, 101))
print(gen_squares)
print(list(gen_squares))
print(list(gen_squares))

# cart_item_count = sum(item[2] for item in cart)
cart_item_count = sum(qty for (name, price, qty) in cart)
print(cart_item_count)

max_item_count = max(item[2] for item in cart)
print(max_item_count)

max_item_price = max(price for name, price, qty in cart)
print(max_item_price)

max_item = max((item for item in cart), key=lambda i: i[1])
print(max_item)

print('---')
food = {
    'coffee': 'beverage',
    'pizza': 'entree',
    'cookie': 'dessert',
    'tea': 'beverage',
}

print('--- dict ---')
beverages = {food: category.upper() for food, category in food.items() if category == 'beverage'}
print(beverages)

print('--- set ---')
categories = {category for category in food.values()}
print(categories)

print('---')
# Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}
newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
print(newTeam)

print('---')
# build a set from an input source
sTemp = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in sTemp if not c.isspace()}
print(chars)

print('--- map vs comprehensions')
# no necessarily faster than the other
print(list(map(str, range(5))))
print([str(i) for i in range(5)])
