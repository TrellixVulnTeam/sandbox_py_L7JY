import abc


class Iterator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def has_next(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass


class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_iterator(self):
        pass


class MyListIterator(Iterator):
    def __init__(self, my_list):
        self.index = 0
        self.list = my_list.list

    def has_next(self):
        return self.index < len(self.list)

    def next(self):
        self.index += 1
        return self.list[self.index - 1]


class MyList(Container):
    def __init__(self, *args):
        self.list = list(args)

    def get_iterator(self):
        return MyListIterator(self)


if __name__ == "__main__":
    my_container: Container = MyList(*range(1, 7))  # Container
    my_iterator: Iterator = my_container.get_iterator()  # Iterator
    while my_iterator.has_next():
        print(my_iterator.next())
