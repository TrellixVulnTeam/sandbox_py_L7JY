from collections.abc import *


def print_supported(cls):
    protocols = [Collection, Container, Iterable, Sized,
                 Sequence, MutableSequence, Reversible,
                 Mapping, MutableMapping,
                 Set, MutableSet]
    supported = [p.__name__ for p in protocols if issubclass(cls, p)]
    print(cls.__name__, supported)


print_supported(list)
print_supported(tuple)
print_supported(dict)
print_supported(set)
