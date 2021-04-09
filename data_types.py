import decimal
import fractions

print("Hello World!")

pi = 3.14159
answer = 42

print(int(pi))
print(float(answer))

print(int("1000", 3))  # base3

print(True)
print(False)
print(int(True))  # => 1
print(int(False))  # => 0
print(str(True))
print(issubclass(bool, int))  # => True

# Falsy
print()
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool("0"))  # => True
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
print(bool(range(0)))
print(bool(decimal.Decimal(0)))
print(bool(fractions.Fraction(0, 10)))
