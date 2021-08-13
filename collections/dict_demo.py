# Dictionary
# changed in Python3.7: remember insertion order

print(dict(a=1, b=2))
print(dict([["name", "hoge"]]))
print(dict((("name", "hoge"),)))
print({
    "b": {"first_name": "hoge", "last_name": "fuga"},
    "c": "3",
    "a": "1",
})

print()

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

print(student["name"])
print(len(student))
# student["last_name"]  # KeyError
print(student.get("last_name"))
print(student.get("last_name", "Unknown"))

# iteration
print(student.keys())  # dict_keys : set-like view
print(student.values())  # dict_values : list-like view
print(student.items())  # dict_items : set-like view of key-value pairs (tuples)

for key in student:  # ↓
    print("key:", key)
for key in student.keys():
    print("key:", key)

for value in student.values():
    print("value:", value)

for key, value in student.items():
    print("{}: {}".format(key, value))

print()

# dict view objects
print(student.keys() == student.keys())
print(student.values() == student.values())  # always False!!
print(student.items() == student.items())

print()

# manipulation
student["name"] = "James"
print(student)
print("name" in student.keys())
print("name" in student)
print(None in student.values())

student.update({"name": "Hoge", "last_name": "Fuga"})  # "upsert(merge)"
print(student)

del student["name"]
print(student)

student.setdefault("class", "A")
print(student)
student.setdefault("class", "B")
print(student)

print(student.pop("last_name"))
print(student)
print(student.popitem())
print(student)

print()

# unpack
dict_a = {"a": 1, "x": 10}
dict_b = {"b": 2, "x": 20}


def func(a, x):
    print(a, x)


print(*dict_a)  # keys
func(**dict_a)
print({**dict_a, **dict_b})  # 3.5 onwards
print({**dict_a, "あ": "ほ", **dict_b})
