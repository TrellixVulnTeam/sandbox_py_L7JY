class SwordMeta(type):

    # subclass instance checking
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    # doesn't check for subclass inheritance
    def __subclasscheck__(cls, sub):
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))


class Sword(metaclass=SwordMeta):
    """virtual base class"""

    def thrust(self):
        print("Thrusting...")


class BroadSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")


class SamuraiSword:

    def swipe(self):
        print("Slice!")

    def sharpen(self):
        print("Shink!")


class Rifle:

    def fire(self):
        print("Bang!")


if __name__ == '__main__':
    print(issubclass(BroadSword, Sword))
    print(issubclass(SamuraiSword, Sword))
    print(issubclass(Rifle, Sword))

    print()
    s = BroadSword()
    print(isinstance(s, Sword))

    print()
    s.swipe()
    # s.thrust()  # NG
    print(BroadSword.mro())
