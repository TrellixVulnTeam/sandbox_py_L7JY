print(type(10))
print(type(10.0))
print(type('a'))
print(type(print))
print(type("Hi there"))
print(type([]))
print(type({}))
print(type(()))

print()
r = range(0, 30)
print(type(r))

if isinstance(r, range):
    print(list(r))

print()

print(type(('hello',)))  # tuple
print(type(('hello')))  # str
print(type(['hello']))  # list
print(type(tuple('hello')))  # tuple

print()


class Car:
    pass


class Truck(Car):
    ...  # Ellipsis


c = Car()
convert = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t))
print(type(c) == type(convert))

print()
print(isinstance(c, Car))
print(isinstance(t, Truck))
print(isinstance(t, Car))
print(issubclass(Truck, Car))

print()
print(issubclass(bool, int))  # True
