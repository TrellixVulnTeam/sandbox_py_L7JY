# Python Logical Operators: And, Or, Not:

# What is a Boolean?
isRaining = False
isSunny = True


# Logical Operators -> Special Operators for Booleans

# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false

if isRaining and isSunny:
    print("We might see a rainbow")

# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false
if isRaining or isSunny:
    print("It might be rainy or it might be sunny")

# NOT
# true --> false
# false --> true
if not isRaining:
    print("It must be raining")


# Python Comparison Operators

# < --> is less than
print(10 < 75)
print(75 < 10)

if 10 < 75:
    print("The bigger number is bigger")

# == --> is equal to
# != --> is not equal to
kitten = 10
tiger = 75

if kitten != tiger:
    print("Not equal")

if kitten < tiger:
    print("The kitten weighs less than the tiger")

# < --> is less than
mouse = 1
if mouse < kitten and mouse < tiger:
    print("The mouse weighs the least")


# False --> 0
# True --> 1
# > --> is greater than
print(False > True)

# Looking for first mismatched letter
# A - Z --> 1 - 26
# > --> is greater than
print("Jennifer" > "Jenny")

# A - Z --> 1 - 26
# <= --> is less than or equal to
print('a' <= 'b')

# ternary
a = 1
b = 2
print("bigger" if a > b else "smaller")

# is
nl1 = [1, 2]
nl2 = [1, 2]
print(id(nl1) == id(nl2))
print(nl1 == nl2)  # => True
print(nl1 is nl2)  # => False

v = None
w = 0
if v == None:
    print("None")
if v is None:
    print("None")
if w != None:
    print("Not None")
if w is not None:
    print("Not None")
