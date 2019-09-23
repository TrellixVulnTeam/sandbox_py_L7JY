# problems in multiple inheritance


class Singleton(object):
    _instances = {}  # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]


class Hoge(Singleton):

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
