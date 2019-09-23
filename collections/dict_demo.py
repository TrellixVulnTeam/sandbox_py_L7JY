# Dictionary

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
print(student.get("last_name", "Unknown"))
print(student.keys())  # dict_keys : like set
print(student.values())  # dict_values : like list
print(student.items())  # dict_items : like set of tuples

for key in student:  # ↓
    print("key:", key)
for key in student.keys():
    print("key:", key)

for value in student.values():
    print("value:", value)

for key, value in student.items():  # list of tuple
    print("{}: {}".format(key, value))

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

print()

# join
dict_a = {"a": 1, "x": 10}
dict_b = {"b": 2, "x": 20}
print({**dict_a, **dict_b})  # 3.5 onwards
print({**dict_a, "あ": "ほ", **dict_b})
