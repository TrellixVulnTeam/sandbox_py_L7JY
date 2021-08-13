"""
Method Resolution Order (MRO)
C3(Graph) algorithm
super(): Bound, Unbound Proxy
  Bound Proxy Object
    super(base-class, derived-class): Class-bound
    super(class, instance-of-class): Instance-bound
"""


class BaseClass:
    def __init__(self):
        print("BaseClass.__init__")

    def __str__(self):
        return self.__class__.__name__

    def call_me(self):
        return "BaseClass.call_me"


class LeftSubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("LeftSubClass.__init__")

    def call_me(self):
        return super().call_me() + " :LeftSubClass.call_me"


class RightSubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("RightSubclass.__init__")

    def call_me(self):
        return super().call_me() + " :RightSubClass.call_me"


class SubClass(LeftSubClass, RightSubClass):
    def __init__(self):
        super().__init__()
        print("SubClass.__init__")

    def call_me(self):
        # super(SubClass, self).call_me()
        return super().call_me() + " :SubClass.call_me"


if __name__ == '__main__':
    s = SubClass()

    print()
    print(SubClass.__bases__)
    print(SubClass.__mro__)
    print(SubClass.mro())

    print()
    # Class-bound proxy
    print(super(LeftSubClass, SubClass))
    print(super(RightSubClass, SubClass))
    print(super(BaseClass, SubClass))

    print()
    # Instance-bound proxy
    print(super(SubClass, s).call_me)
    print(super(LeftSubClass, s).call_me)
    print(super(RightSubClass, s).call_me)

    print()
    print(s.call_me())
    print(super(SubClass, s).call_me())
    print(super(LeftSubClass, s).call_me())
    print(super(RightSubClass, s).call_me())
