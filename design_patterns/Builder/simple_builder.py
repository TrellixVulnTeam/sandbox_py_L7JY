from abc import ABCMeta, abstractmethod


class Builder(object, metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = Product()


class Director(object, metaclass=ABCMeta):
    def __init__(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class Product(object):
    def __init__(self):
        self.var1 = None

    def __str__(self):
        return self.var1


class ConcreteBuilder(Builder):
    def set_var1(self, var1):
        self.constructed_object.var1 = var1


class ConcreteDirector(Director):
    def construct(self):
        builder.set_var1('Hoge')


if __name__ == '__main__':
    builder = ConcreteBuilder()
    director = ConcreteDirector(builder)
    director.construct()
    product = director.get_constructed_object()
    print(product)
