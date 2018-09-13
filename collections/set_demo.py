# Set : no duplicated, sorted by natural order

s = {7, 11, 13, 5, 3, 1}
print(s)

d = {}  # !! dict !!

s.add(17)
s.add(17)
print(s)
s.update({23, 19}, {29, 2})
print(s)
s.add(15)
print(s)
s.remove(15)
print(s)
# s.remove(100)  # KeyError
s.discard(100)  # no Exception : listにはない

while s:
    print(s.pop() / 3)
print(s)

print()

# 集合演算
x = set('hogehoge')
y = set('abcdefg')
print(x)
print(y)
print(x | y)  # or
print(x.union(y))
print(x & y)  # and
print(x.intersection(y))
print(x - y)  # sub
print(x.difference(y))
print(x ^ y)  # xor
print(x.symmetric_difference(y))
print((x | y) - (x & y))

print()

set1 = {0, 1}
set2 = {2, 0, 1}
print(set1.issubset(set2))  # 真部分集合
print(set1 < set2)
print(set2.issuperset(set1))
print(set2 > set1)
set1.add(2)  # set1 = {0, 1, 2}
print(set1.issubset(set2))  # 部分集合（同値を含む）
print(set1 < set2)
print(set1 <= set2)
print(set2.issuperset(set1))
print(set2 > set1)
print(set2 >= set1)

set3 = {3, 6, 9}
print(set3.isdisjoint(set1))
