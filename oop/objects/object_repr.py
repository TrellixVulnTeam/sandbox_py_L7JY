# customize string representations of objects
import reprlib


class Person:
    def __init__(self, fname="Nanasi", lname="Gonbei", age=0):
        self.fname = fname
        self.lname = lname
        self.age = age

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age:{2}>".format(self.fname, self.lname, self.age)

    # use str for a more human-readable string
    # not overridden, __repr__ is used
    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))

    # default: __str__()
    def __format__(self, format_spec):
        if format_spec == 'q':
            return "{0}, {1}: {2}".format(self.fname, self.lname, self.age)
        else:
            return "{1}, {0}".format(self.fname, self.lname)


def main():
    # create a new Person object
    p1 = Person("ほげ", "ふが", 25)

    # use different Python functions to convert it to a string
    print(p1)
    print(repr(p1))
    print(str(p1))
    print("Formatted: {0}".format(p1))
    print("Formatted: {0:q}".format(p1))
    print("Formatted: {0!r}".format(p1))  # force repr
    print("Formatted: {0!s}".format(p1))  # force str
    print(bytes(p1))

    print()

    people = [Person("Hoge", "Fuga", a) for a in range(100)]

    print(repr(people))
    print(reprlib.repr(people))


if __name__ == "__main__":
    main()
