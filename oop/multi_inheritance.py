class BaseClass:
    call_list = []

    def __init__(self):
        print("BaseClass")

    def call_me(self):
        print("Calling method on Base Class")
        self.call_list.append("BaseClass")


class LeftSubclass(BaseClass):
    def __init__(self):
        print("LeftSubclass")

    def call_me(self):
        print("Calling method on Left Subclass")
        super().call_me()
        self.call_list.append("LeftSubclass")


class RightSubclass(BaseClass):
    def __init__(self):
        print("RigthSubclass")

    def call_me(self):
        print("Calling method on Right Subclass")
        super().call_me()
        self.call_list.append("RightSubclass")


class Subclass(LeftSubclass, RightSubclass):
    # def __init__(self):
    #     print("Subclass")

    def call_me(self):
        print("Calling method on Subclass")
        super().call_me()
        self.call_list.append("Subclass")


s = Subclass()
s.call_me()
print(s.call_list)
print(Subclass.mro())
