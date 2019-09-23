# class variable vs instance variable


class Hoge:  # == Hoge(object, metaclass=type)
    # class doesn't introduce new scope
    attr = 0

    @classmethod
    def _get_cls_attr(cls):
        return cls.attr

    @classmethod
    def _set_cls_attr(cls, value):
        cls.attr = value


class Fuga(Hoge):
    attr = 100

    def access_attr(self):
        print(self.attr)  # class
        self.attr += 1  # shadow instance variable
        print(self.attr)  # instance
        print(self._get_cls_attr())
        self._set_cls_attr(33)
        print(self._get_cls_attr())


if __name__ == '__main__':
    f = Fuga()
    f.access_attr()
    print()
    print(f.attr)
    print(Fuga.attr)
    print(Hoge.attr)
