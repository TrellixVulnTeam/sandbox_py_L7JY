"""
attribute lookup precedence
 1. data descriptor
 2. instance attribute in __dict__
 3. non-data descriptor
"""


class DataDescriptor:

    def __get__(self, instance, owner):
        print("DataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))

    def __set__(self, instance, value):
        print("DataDescriptor.__set__({!r}, {!r}, {!r})"
              .format(self, instance, value))


class NonDataDescriptor:

    def __get__(self, instance, owner):
        print("NonDataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))


class Owner:
    a = DataDescriptor()
    b = NonDataDescriptor()


if __name__ == '__main__':
    obj = Owner()
    print(obj.a)
    obj.__dict__['a'] = 19683
    print(obj.a)  # data descriptor

    print()
    print(obj.b)
    obj.__dict__['b'] = 19683
    print(obj.b)  # instance attribute
