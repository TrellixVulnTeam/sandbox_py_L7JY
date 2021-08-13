class Hoge:
    """Decorator"""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a str")
        self._name = name.capitalize()


class HogeChild(Hoge):
    @Hoge.name.setter
    def name(self, name: str):
        Hoge.name.fset(self, f"*** {name} ***")


class Fuga:
    """Property object"""

    def _get_name(self):
        return self._name

    def _set_name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a str")
        self._name = name.capitalize()

    name = property(fget=_get_name, fset=_set_name)
    # name = property(fset=_set_name)  # setter only property


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
        """deleter"""
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

    h2 = HogeChild()
    h2.name = "hoge jr"
    print(h2.name)
    h2.name = 9

    piyo1 = Piyo()
    piyo1.first_name = "piyo1"
    piyo1.last_name = "piyo1"
    print(piyo1)

    piyo2 = Piyo()
    piyo2.first_name = "piyo2"
    piyo2.last_name = "piyo2"
    print(piyo2)
