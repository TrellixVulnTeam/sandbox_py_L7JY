from collections.abc import *

# list
print(issubclass(list, Container))
print(issubclass(list, Sequence))
print(issubclass(list, Mapping))
print(issubclass(list, Sized))
print(issubclass(list, Iterable))

print()

# tuple
print(issubclass(tuple, Container))
print(issubclass(tuple, Sequence))
print(issubclass(tuple, Mapping))
print(issubclass(tuple, Sized))
print(issubclass(tuple, Iterable))

print()

# dict
print(issubclass(dict, Container))
print(issubclass(dict, Sequence))
print(issubclass(dict, Mapping))
print(issubclass(dict, Sized))
print(issubclass(dict, Iterable))

print()

# set
print(issubclass(set, Container))
print(issubclass(set, Sequence))
print(issubclass(set, Mapping))
print(issubclass(set, Set))
print(issubclass(set, Sized))
print(issubclass(set, Iterable))
