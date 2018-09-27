from abc import ABCMeta


class Sword(metaclass=ABCMeta):
    """virtual base class"""

    @classmethod
    def __subclasshook__(cls, sub):  # return True, False, NotImplemented
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                 and
                 hasattr(sub, 'sharpen') and callable(sub.sharpen))
                or NotImplemented)

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


@Sword.register
class LightSaber:

    def swipe(self):
        print("Ffffkrrrrshhzzzwooooom..woom..woooom..")


class Rifle:

    def fire(self):
        print("Bang!")


if __name__ == '__main__':
    print(issubclass(BroadSword, Sword))
    print(issubclass(SamuraiSword, Sword))
    print(issubclass(Rifle, Sword))
    print(issubclass(LightSaber, Sword))

    print()
    s = BroadSword()
    print(isinstance(s, Sword))

    print()
    s.swipe()
    # s.thrust()  # NG
    print(BroadSword.mro())
