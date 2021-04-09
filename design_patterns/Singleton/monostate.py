class MonoState(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__dict__ = cls._state
        return self


class Hoge(MonoState):

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
