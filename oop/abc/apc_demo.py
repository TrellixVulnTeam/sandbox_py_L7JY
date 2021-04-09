from collections.abc import MutableSequence, Hashable
from abc import ABCMeta, ABC, abstractmethod

print(issubclass(list, MutableSequence))  # True
print(list.__mro__)  # no MutableSequence

# ms = MutableSequence()  # NG

print()
print(issubclass(object, Hashable))  # True
print(issubclass(list, object))  # True
print(issubclass(list, Hashable))  # False!
print(object.__hash__)
print(list.__hash__)  # None : removed

object.__subclasshook__()  # NotImplemented

print()


class Text(metaclass=ABCMeta):
    pass


Text.register(str)
print(issubclass(str, Text))  # True
print(isinstance("Hoge Hoge", Text))  # True


@Text.register
class Prose:
    pass


print(issubclass(Prose, Text))  # True

print()


class AbstractBaseClass(ABC):

    @property
    @abstractmethod
    def abstract_property(self):
        raise NotImplementedError

    @property
    def conrete_property(self):
        return "sand, cement, water"


print(AbstractBaseClass.abstract_property.__isabstractmethod__)
print(AbstractBaseClass.conrete_property.__isabstractmethod__)
