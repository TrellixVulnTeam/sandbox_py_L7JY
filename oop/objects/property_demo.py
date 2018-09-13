class Hoge:
    """ Decorator """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a str")
        self._name = name.upper()


class Fuga:
    """ Property object """

    def _get_name(self):
        return self._name

    def _set_name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a str")
        self._name = name.upper()

    name = property(fget=_get_name, fset=_set_name)


class UpperStr:
    """ Descriptor """

    def __init__(self):
        from weakref import WeakKeyDictionary
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._instance_data[instance]

    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise ValueError("Value {} is not str".format(value))
        self._instance_data[instance] = value.upper()

    def __delete__(self):
        raise AttributeError("Cannot delete attribute")


class Piyo:
    name = UpperStr()  # bound to class attribute


if __name__ == '__main__':
    h = Hoge()
    h.name = "hoge"
    print(h.name)
    # h.name = 9

    f = Fuga()
    f.name = "fuga"
    print(f.name)
    # f.name = 9

    p = Piyo()
    p.name = "piyo"
    print(p.name)
    # p.name = 9
