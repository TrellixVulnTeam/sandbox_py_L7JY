# Tuple : immutable sequence

tuple1 = (1, 2)
tuple2 = 1, 2
not_tuple = (5)
print(type(not_tuple))
tuple3 = (5,)
print(type(tuple3))

print()


def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add(5, 5))
print(add(32))

print()

subjects = ('Python', 'Coding', 'Tips')
subjects2 = ('Python', 'Coding', 'Tips')
print(subjects == subjects2)  # => True
print(id(subjects) == id(subjects2))  # => False : stringとは違う点
print(subjects is subjects2)  # => False

print()

z = ["hoge"]
c = (1, z, 2)
d = c[:]
z += ["fuga"]
print(c)
print(d)

print()

# multiple assignment
tt = (a, (b, (c, d))) = (4, (3, (2, 1)))
print(a, b, c, d)
print(tt)

# swapping technique
s = 5
t = 20
s, t = t, s
print(s, t)
