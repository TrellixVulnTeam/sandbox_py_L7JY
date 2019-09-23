import abc
from collections.abc import Iterable
from datetime import date
from functools import reduce


class AbsComponent(metaclass=abc.ABCMeta):
    """ Component """

    @abc.abstractmethod
    def get_oldest(self):
        pass


class Person(AbsComponent):
    """ Leaf node """

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def get_oldest(self):
        return self


class NullPerson(AbsComponent):
    """ Leaf node """
    name = None
    birthdate = date.max

    def get_oldest(self):
        return self


class Tree(Iterable, AbsComponent):
    """ Composite node """

    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)

    def get_oldest(self):
        def f(t1, t2):
            t1_, t2_ = t1.get_oldest(), t2.get_oldest()
            return t1_ if t1_.birthdate < t2_.birthdate else t2_

        return reduce(f, self, NullPerson())


if __name__ == '__main__':
    hitchhikers = Tree([
        Person('Trillian', date(1970, 3, 14)),
        Person('Arthur', date(1965, 7, 4)),
        Person('Ford', date(1995, 2, 2)),
        Person('Zaphod', date(1997, 5, 1)),
        Person('Douglas', date(1999, 4, 2))
    ])

    singles = Tree([
        Person('Marvin', date(1991, 1, 1)),
        Person('Slarti', date(1993, 9, 9))
    ])

    loner = Person('Dirk', date(1990, 6, 6))

    tree1 = Tree([hitchhikers])
    tree2 = Tree([singles, loner])
    tree3 = Tree([tree1, tree2])

    for tree in tree1, tree2, tree3:
        oldest = tree.get_oldest()
        max_age = (date.today() - oldest.birthdate).days / 365.2425
        print('Oldest person: {}; Age: {:6.2f}'.format(oldest.name, max_age))
