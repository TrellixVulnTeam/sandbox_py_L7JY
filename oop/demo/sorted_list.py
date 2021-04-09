# Multiple inheritance
class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass


if __name__ == '__main__':
    print(SortedIntList.__bases__)
    print(SortedIntList.__mro__)
    print(SortedIntList.mro())

    print()

    # Class-bound proxy
    print(super(IntList, SortedIntList))
    print(super(SortedList, SortedIntList))
    print(super(SimpleList, SortedIntList))

    # can call static or class method
    print(super(SortedIntList, SortedIntList)._validate(5))

    # Instance-bound proxy
    ins = SortedIntList([5, 15, 10])
    print(super(IntList, ins))
    print(super(SortedList, ins))
    print(super(SimpleList, ins))

    print(super(SortedIntList, ins).add)
    print(super(IntList, ins).add)
    print(super(SortedList, ins).add)

    super(IntList, ins).add(1)
    print(ins)
    super(SortedList, ins).add('a')
    print(ins)

    print()
    sl = SortedIntList()
    print(isinstance(sl, SortedIntList))
    print(isinstance(sl, SimpleList))
    print(isinstance(sl, SortedList))
    print(isinstance(sl, IntList))

    print()
    print(issubclass(SortedIntList, SortedIntList))
    print(issubclass(SortedIntList, SimpleList))
    print(issubclass(SortedIntList, SortedList))
    print(issubclass(SortedIntList, IntList))

    print()
    sl.add(2)
    sl.add(7)
    sl.add(1)
    sl.add(5)

    try:
        sl.add('a')
    except TypeError as e:
        print(repr(e))

    print(sl)
