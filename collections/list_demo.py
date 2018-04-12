# List demo

list1 = list(range(1, 10))
print(list1)

list1.append(10)
print(list1)

print()

# slices
# [start:end:step]
print(list1[1:5])
print(list1[0:3])
print(list1[:3])
print(list1[3:])
print(list1[-1])
print(list1[-1:])
print(list1[:-1])
print(list1[::2])
print(list1[::-1])
list2 = list1[:]  # copy
print(list2 is list1)
del list2[0]
print(list2)
print(list1)

list2[1:2] = ['a', 'b', 'c']
print(list2)

list2[:] = list1  # copy elements 1 by 1
print(list2)
print(list2 is list1)

list2[-1] = "hoge"
print(list2)

list2[-1:] = "hoge"  # string is also iterable
print(list2)

list2[-4:] = ["".join(list2[-4:])]
print(list2)

print()

# shallow copy
e = ["hoge"]
a = [5, e, 6]
b = a[:]
print(b)
e += ["fuga"]
print(b)
print(a)

print()

# operators
print(list1 + ['a', 'b'])
print(list1 * 2)

print()

# methods
l = [1, 2, 3]
l.extend("abc")  # => l += ['a', 'b', 'c']
print(l)
l.insert(3, 'x')
print(l)
del l[2:4]
print(l)
l.remove('b')
print(l)

print()

l1 = [(7, 2), (3, 4), (5, 5), (10, 3)]
l2 = sorted(l1, key=lambda x: x[1])
print(l2)  # [(7, 2), (10, 3), (3, 4), (5, 5)]

print()

# enumerate
print(list(enumerate("qwerty")))

for i, v in enumerate("qwerty"):
    print("{}: {}".format(i, v))

for i, v in enumerate("qwerty", start=10):
    print("{}: {}".format(i, v))
