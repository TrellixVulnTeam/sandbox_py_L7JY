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
s.discard(100)  # no Exception

while s:
    print(s.pop() / 3)
print(s)

# 集合演算
x = set('hogehoge')
y = set('abcdefg')
print(x)
print(y)
print(x | y)  # or : union
print(x & y)  # and: intersection
print(x - y)  # sub: difference
print(x ^ y)  # xor: symmetric difference => (x | y) - (x & y)

set1 = {0, 1}
set2 = {2, 0, 1}
print(set1.issubset(set2))  # 真部分集合
set1.add(2)
print(set1.issubset(set2))  # 部分集合（同値を含む）
