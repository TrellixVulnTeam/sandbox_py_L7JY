import random


class Sneaky:
    sneaky = True

    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(super())
        self.sneaky = sneaky

    def hide(self, light_level):
        return self.sneaky and light_level < 10


class Agile:
    agile = True

    def __init__(self, agile=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(super())
        self.agile = agile

    def evade(self):
        return self.agile and random.randint(0, 1)


class Character:
    def __init__(self, name=None, **kwargs):
        if not name:
            raise ValueError("'name' is required")
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)


class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))


if __name__ == '__main__':
    hoge = Thief(name="Hoge", sneaky=False)  # 多重継承の場合は、positionalに頼るべきではない。
    print(hoge)
    print(hoge.sneaky)
    print(hoge.agile)
    print(hoge.hide(8))
