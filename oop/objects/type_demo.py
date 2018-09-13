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
    def __init__(self, name="", color=""):
        self.name = name
        self.color = color

    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self.name, self.color)


class Truck(Car):
    pass


c = Car("Hoge", "Red")
convert = Car()
t = Truck()
print(c.__class__)
print(c.__class__.__name__)
print(type(c))
print(type(t))
print(type(c) == type(t))
print(type(c) == type(convert))

print()
print(isinstance(c, Car))
print(isinstance(t, Truck))
print(isinstance(t, Car))
print(issubclass(Truck, Car))
print(issubclass(Truck, Truck))  # True

print()
print(issubclass(bool, int))  # True
print(isinstance(True, int))  # True

print()
print(dir(c))
print(c.__dict__)
print(type(c.__dict__))  # dict
print(vars(c))
print(len(c))  # duck typing

print()
i = 7
print(type(i))
print(i.__class__)
print(i.__class__.__class__)
print(i.__class__.__class__.__class__)
print(issubclass(type, object))
print(type(object))  # class object type is 'type'
print(type(type))

print(dir(i))
print(getattr(i, 'denominator'))
print(getattr(i, 'numerator'))
print(getattr(i, 'conjugate'))
print(callable(getattr(i, 'conjugate')))
print(i.conjugate.__class__.__name__)
print(hasattr(i, 'bit_length'))  # use exception handler internal
print(hasattr(i, 'index'))

print(i.__class__.__dict__)
print(type(i.__class__.__dict__))  # not dict object
print(i.__class__.__dict__['__repr__'](i))
