# better way


class SingletonMeta(type):
    _instances = {}  # dict([cls, instance])

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Hoge(metaclass=SingletonMeta):

    # metaclassの場合は2回目以降は実行されない
    def __init__(self, val):
        self.val = val
        print('Hoge.__init__')

    def __str__(self):
        return "{0!r} {1}".format(self, self.val)


if __name__ == '__main__':
    h1 = Hoge('hoge1')
    print(h1)
    h2 = Hoge('hoge2')
    print(h2)
    h2.val = 'hoge2-re'
    print(h1)
    print(h2)
