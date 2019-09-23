import abc


class AbsComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass


class Leaf(AbsComponent):
    def __init__(self, name, *args, **kwargs):
        self.name = name

    def operation(self):
        print(self.name)


class Composite(AbsComponent):
    def __init__(self, *args, **kwargs):
        self.children = []

    def operation(self):
        for child in self.children:
            child.operation()

    def get_child(self, idx):
        return self.children[idx]

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)


if __name__ == '__main__':
    composite = Composite()
    root = Composite()
    composite.add(Leaf('Leaf in composite 1'))
    composite.add(Leaf('Leaf in composite 2'))
    root.add(composite)
    root.add(Leaf('Leaf in root'))
    root.operation()
