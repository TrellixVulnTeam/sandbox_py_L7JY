class Hoge:
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
        self.va = Hoge.cls_attr


class Fuga(Hoge):
    cls_attr = 100


def main():
    pass


if __name__ == '__main__':
    main()
