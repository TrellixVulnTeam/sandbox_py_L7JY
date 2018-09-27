class Hoge:
    """ Decorator """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a str")
        self._name = name.capitalize()


class Fuga:
    """ Property object """

    def _get_name(self):
        return self._name

    def _set_name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a str")
        self._name = name.capitalize()

    name = property(fget=_get_name, fset=_set_name)


class CapitalizeStr:
    """Descriptor"""

    def __init__(self):
        from weakref import WeakKeyDictionary
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        """getter"""
        if instance is None:
            return self
        return self._instance_data[instance]

    def __set__(self, instance, value: str):
        """setter"""
        if not isinstance(value, str):
            raise ValueError("Value {} is not str".format(value))
        self._instance_data[instance] = value.capitalize()

    def __delete__(self):
        """deleter : del()"""
        raise AttributeError("Cannot delete attribute")


class Piyo:
    first_name = CapitalizeStr()  # bound to class attribute
    last_name = CapitalizeStr()  # bound to class attribute

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


if __name__ == '__main__':
    h = Hoge()
    h.name = "hoge"
    print(h.name)
    # h.name = 9

    f = Fuga()
    f.name = "fuga"
    print(f.name)
    # f.name = 9

    fefe = Piyo()
    fefe.first_name = "fefe"
    fefe.last_name = "fefe"
    print(fefe)
