class Hoge:  # == Hoge(object, metaclass=type)
    # Class doesn't introduce new scope
    cls_attr = 0

    @classmethod
    def _get_cls_attr(cls):
        return cls.cls_attr

    @classmethod
    def create_empty(cls):
        return cls(a=None, b=None)

    @classmethod
    def create_with_items(cls, items):
        return cls(**items)

    def __init__(self, *args, **kwargs):
        self.ins_attr = Hoge.cls_attr


class Fuga(Hoge):
    cls_attr = 100

    def __init__(self):
        super().__init__()

    def access_cls_attr(self):
        print(self.cls_attr)  # class
        self.cls_attr += 1  # shadow instance variable
        print(self.cls_attr)
        print(self._get_cls_attr())


if __name__ == '__main__':
    f = Fuga()
    f.access_cls_attr()
