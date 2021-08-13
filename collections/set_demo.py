# Set : no duplicated

s = {7, 11, 3, 1}
print(s)

d = {}  # !! dict !!
empty_set = set()

s.add(17)
s.add(17)
print(s)
s.update({23, 19}, (2, 2, 3))
print(s)
s.add(15)
print(s)
s.remove(15)
print(s)
# s.remove(100)  # KeyError
s.discard(100)  # no Exception : listにはない

# pop
while s:
    print(s.pop())
print(s)

print()

# 集合演算
x = set('abcdefg')
y = set('defghij')
print(x)
print(y)

# method version accepts not only a set but an iterable

print(x | y)  # or
print(x.union(y))

print(x & y)  # and
print(x.intersection(y))

print(x - y)  # sub
print(x.difference(y))
print(y - x)

print(x ^ y)  # xor
print(x.symmetric_difference(y))
print((x | y) - (x & y))

print()

# 真部分集合（proper subset）
set1 = {0, 1}
set2 = {2, 0, 1}
print(set1 < set2)
print(set2 > set1)

# 部分集合（同値を含む）
set1 = {0, 1, 2}
set2 = {2, 0, 1}
print(set1 == set2)
print(set1 < set2)
print(set1 <= set2)
print(set1.issubset(set2))
print(set2 > set1)
print(set2 >= set1)
print(set2.issuperset(set1))

set3 = {3, 6, 9}
print(set3.isdisjoint(set2))  # no intersection

print()

# unpack
set_x = {5, 10}
set_y = {2, 5}
print({*set_x, *set_y})
print({*set_x, "あ", "ほ", *set_y})

print()

# frozenset
set_a = {1, 3, 5, 7}
set_b = frozenset(set_a)
print(dir(set_a))
print(dir(set_b))
