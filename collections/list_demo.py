# List : mutable sequence

list1 = list(range(10))
print(list1)
print(list1.__len__())
print(len(list1))  # preferred

list1.append(10)
print(list1)

print()

# slices (sequence protocol)
# [start:end:step]
print(list1[1:5])
print(list1[0:3])
print(list1[:3])
print(list1[3:])
print(list1[-1])  # not slice, single value
print(list1[-1:])
print(list1[:-1])
print(list1[::2])
print(list1[::-1])
list2 = list1[:]  # shallow copy
print(list2 is list1)
del list2[0]
print(list2)
del list2[2:4]
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
list3 = ['a', 'b']
print(list3 + ['c'])
print(list3 * 2)
print(list3)

list4 = [[1]] * 4
print(list4)
list4[0].append(2)
print(list4)

print()

# methods
l = [1, 2, 3]
l.extend("abc")  # => l += ['a', 'b', 'c']
print(l)
print(l.index('c'))
l.insert(3, 'x')
print(l)
l.remove('b')
print(l)
l.reverse()
print(l)

l = [[5, 8], {6, 3, 7}, (2, 9), [100]]
l.sort(key=sum, reverse=True)  # key: func (len, sum, ...)
print(l)
print(list(map(sum, l)))

print()

# out-of-place
l1 = [(7, 2), (3, 4), (5, 5), (10, 3)]
l2 = sorted(l1, key=lambda x: x[1])
print(l2)  # => [(7, 2), (10, 3), (3, 4), (5, 5)]
l3 = reversed(l1)
print(l3)
print(list(l3))

print()

# enumerate
print(list(enumerate("qwerty")))

for i, v in enumerate("qwerty"):
    print("{}: {}".format(i, v))

for i, v in enumerate("qwerty", start=10):
    print("{}: {}".format(i, v))

print()

# unpack
list_x = [5, 10]
list_y = [2, 5]
print([*list_x, *list_y])
print([*list_x, "あ", "ほ", *list_y])
