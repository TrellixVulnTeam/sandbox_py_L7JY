# Custom Collection class
# immutable SortedSet
from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain


class SortedSet(Set, Sequence):

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        """container, sequence, set"""
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        """sized, sequence, set"""
        return len(self._items)

    def __iter__(self):
        """iterable"""

        # generator function
        # for item in self._items:
        #     yield item

        # another way (3.3~)
        # yield from self._items

        # simple way
        return iter(self._items)

    def __getitem__(self, index):
        """iterable, sequence"""
        result = self._items[index]
        # indexがsliceオブジェクトの場合、listではなくSortedSetを返すようにする
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented  # raise NotImplementedErrorではない
        return self._items == rhs._items

    # __eq__をひっくり返すだけなら、わざわざオーバーライドする必要はない
    # def __ne__(self, rhs):
    #     if not isinstance(rhs, SortedSet):
    #         return NotImplemented
    #     return self._items != rhs._items

    def _is_unique_and_sorted(self):
        return all(self[i] < self[i + 1] for i in range(len(self) - 1))

    def index(self, item, start=..., stop=...):
        # assert self._is_unique_and_sorted()
        index = bisect_left(self._items, item)
        if index != len(self._items) and self._items[index] == item:
            return index
        raise ValueError("{} not found".format(repr(item)))

    def count(self, item):
        # assert self._is_unique_and_sorted()
        return int(item in self)  # self.__contains__

    def __add__(self, rhs):
        """sequence"""
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs):
        """sequence"""
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        """sequence"""
        return self * lhs  # self.__mul__

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)


if __name__ == '__main__':
    # count及びindexをオーバーライドしたときの比較
    # Linear Search (O(n)) vs Binary Search (O(logN))
    from random import randrange
    from timeit import timeit

    s = SortedSet(randrange(1000) for _ in range(2000))
    print(len(s))
    time = timeit(setup='from __main__ import s',
                  stmt='[s.count(i) for i in range(1000)]',
                  number=100)
    print(time)

"""
# run from the command line
python -O -m timeit -n 1 -s "from random import randrange; from sorted_set import SortedSet; s = SortedSet(randrange(1000) for _ in range(2000))" "[s.count(i) for i in range(1000)]"
"""
