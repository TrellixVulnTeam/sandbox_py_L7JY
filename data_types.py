"""
docstring
"""

print("Hello World!")

pi = 3.14159
answer = 42

print(int(pi))
print(float(answer))

print(True)
print(False)
print(int(True))  # => 1
print(int(False))  # => 0
print(str(True))
print(issubclass(bool, int))  # => True

# Falsy
print(bool(0))
print(bool(""))
print(bool("0"))  # => True
print(bool(None))
print(bool([]))

print(3 / 2)  # => 1.5
print(3 // 2)  # => 1
print(-3 / 2)  # => -1.5
print(-3 // 2)  # => -2
