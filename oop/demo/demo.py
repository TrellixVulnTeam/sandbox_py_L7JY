from auto_repr import auto_repr


@auto_repr
class Hoge:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


h = Hoge("Hoge")
print(vars(h))
print(h)

h = Hoge(5.1)
print(vars(h))
print(h)
