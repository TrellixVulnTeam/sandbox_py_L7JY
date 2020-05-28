class ExampleIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        rslt = self.data[self.index]
        self.index += 1
        return rslt


class ExampleIterable:
    def __init__(self, data=[]):
        self.data = data

    def __iter__(self):
        return ExampleIterator(self.data)


class AlternateIterable:
    def __init__(self, data=[]):
        self.data = data

    # indexer
    def __getitem__(self, idx):
        return self.data[idx]


if __name__ == '__main__':
    iter_obj = ExampleIterable([1, 2, 3])

    for i in iter_obj:
        print(i)

    for i in enumerate(iter_obj):
        print(i)

    # print(iter_obj)  # NG

    print()

    iter_obj = AlternateIterable([1, 2, 3])

    for i in iter_obj:
        print(i)

    for i in enumerate(iter_obj):
        print(i)

    print(iter_obj[1])  # access by the index
