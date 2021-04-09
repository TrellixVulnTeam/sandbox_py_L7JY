# class variable vs instance variable


class MyClass:
    """The pitfall of accessing class attr by 'self'"""
    b = "on class"

    def __init__(self):
        self.a = "on instance"
        print("self.a:", self.a)
        print("self.b:", self.b)  # class attr
        print("MyClass.b:", MyClass.b)
        self.a = "re-bound"
        self.b = "new on instance"
        print("self.a:", self.a)
        print("self.b:", self.b)  # instance attr
        print("MyClass.b:", MyClass.b)


class Hoge:  # == Hoge(object, metaclass=type)
    # class doesn't introduce new scope
    attr = 0

    __data = None

    @classmethod
    def _get_cls_attr(cls):
        return cls.attr

    @classmethod
    def _set_cls_attr(cls, value):
        cls.attr = value

    @staticmethod
    def get_data():
        if Hoge.__data is None:
            Hoge.__data = []
        return Hoge.__data


class Fuga(Hoge):
    attr = 100

    def access_attr(self):
        print(self._get_cls_attr())
        self._set_cls_attr(33)
        print(self._get_cls_attr())


if __name__ == '__main__':
    m = MyClass()

    print()
    f = Fuga()
    f.access_attr()

    print()
    print(Fuga.attr)
    print(Hoge.attr)

    print()
    Fuga.get_data().append('Fuga')
    print(Hoge.get_data())
