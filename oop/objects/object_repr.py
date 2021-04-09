# customize string representations of objects
import reprlib


class Person:
    def __init__(self, fname="Nanasi", lname="Gonbei", age=0):
        self.fname = fname
        self.lname = lname
        self.age = age

    # use __repr__() to create a string useful for debugging
    # Typically, object creation form string
    def __repr__(self):
        return "{0}(fname='{1}', lname='{2}', age={3})" \
            .format(type(self).__name__, self.fname, self.lname, self.age)

    # use str for a more human-readable string
    # not overridden, __repr__() is used instead
    def __str__(self):
        return "Person: {0} {1} is {2}".format(self.fname, self.lname, self.age)

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return val.encode('utf-8')

    # not overridden, __str__() is used instead
    def __format__(self, format_spec):
        if format_spec == 'q':
            return "{0}, {1}: {2}".format(self.fname, self.lname, self.age)
        else:
            return "{1}, {0}".format(self.fname, self.lname)


def main():
    p1 = Person("ほげ", "ふが", 25)
    print(p1)  # str
    print(str(p1))
    print(repr(p1))
    print(format(p1))
    print(format(p1, 'q'))
    print(bytes(p1))

    p2 = eval(repr(p1))
    print(p2)

    print("Formatted: {0}".format(p1))  # format
    print("Formatted: {0:q}".format(p1))  # format:'q'
    print("Formatted: {0!r}".format(p1))  # repr
    print("Formatted: {0!s}".format(p1))  # str

    print(f"{p1=}")  # repr with var name

    print()

    people = [Person("Hoge", "Fuga", a) for a in range(20)]
    print(repr(people))
    print(reprlib.repr(people))


if __name__ == "__main__":
    main()
