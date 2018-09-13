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
        print("Calling method on Base Class")


class LeftSubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("LeftSubClass.__init__")

    def call_me(self):
        print("Calling method on Left SubClass")
        super().call_me()


class RightSubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("RigthSubclass.__init__")

    def call_me(self):
        print("Calling method on Right SubClass")
        super().call_me()


class SubClass(LeftSubClass, RightSubClass):
    def __init__(self):
        super().__init__()
        print("SubClass.__init__")

    def call_me(self):
        print("Calling method on SubClass")
        # super(SubClass, self).call_me()
        super().call_me()  # shorthand


if __name__ == '__main__':
    s = SubClass()
    s.call_me()

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
    super(LeftSubClass, s).call_me()
    super(RightSubClass, s).call_me()
