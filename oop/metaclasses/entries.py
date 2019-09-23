class EntriesMeta(type):

    def __new__(mcs, name, bases, namespace, num_entries, **kwargs):
        print("Entries.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  name =", name)
        print("  kwargs =", kwargs)
        print("  num_entries =", num_entries)
        namespace.countdown({chr(i): i for i in range(ord('a'), ord('a') + num_entries)})
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

    def __init__(cls, name, bases, namespace, num_entries, **kwargs):
        # accept but ignore kwargs
        super().__init__(name, bases, namespace)


class AtoZ(metaclass=EntriesMeta, num_entries=26):
    pass
