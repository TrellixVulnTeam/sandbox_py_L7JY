"""
hoge
"""

# List
student_names = ["Mark", "Katarina", "Jessica"]

print(student_names[0])
print(student_names[2])
print(student_names[-1])

student_names.append("Homer")  # Add to the end
print("Mark" in student_names)  # Mark is still there!
print("Hoge" not in student_names)  # Hoge is not there!
print(len(student_names))  # How many elements in the list
del student_names[2]  # Jessica is no longer in the list :(

print(student_names)
print(student_names[1:])
print(student_names[1:-1])
print(student_names)  # original has no chaneges

hoge = student_names
del hoge[0]
print(student_names)  # original changed

for name in student_names:
    print("Student name is {0}".format(name))

for i, name in enumerate(student_names):
    print(i, name)

print()
l1 = [(7, 2), (3, 4), (5, 5), (10, 3)]
l2 = sorted(l1, key=lambda x: x[1])
print(l2)  # [(7, 2), (10, 3), (3, 4), (5, 5)]


# tuple : immutable
subjects = ('Python', 'Coding', 'Tips')
subjects2 = ('Python', 'Coding', 'Tips')
print(subjects == subjects2)  # => True
print(id(subjects) == id(subjects2))  # => False : stringとは違う点
print(subjects is subjects2)  # => False


# List & Set
a = ['fugafuga']
print(a)

b = list('fugafuga')  # 注意
print(b)

w = {'hogehoge'}
print(w)

x = set('hogehoge')  # 注意
print(x)

y = set('abcdefg')
print(x - y)
print(x ^ y)
print(x & y)
print(x | y)


# Dictionary
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

print(student["name"])
# student["last_name"]  # KeyError
print(student.get("last_name", "Unknown"))
print(student.keys())  # dict_keys : like set
print(student.values())  # dict_values : like list
print(student.items())  # dict_items : like set of tuples
student["name"] = "James"
print(student)
print("name" in student.keys())
print("name" in student)
print(None in student.values())

del student["name"]
print(student)

student.setdefault("class", "A")
print(student)
student.setdefault("class", "B")
print(student)

print()

# slice
x = {'hoge': ('a', 'x', 100)}
a = [5, x, 6]
b = a[:]  # shallow copy
print(b)
x['hoge'] = ('b', 'y', 200)
print(b)
