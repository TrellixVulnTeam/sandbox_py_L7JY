# __new__ demo
class Hoge:
    # implicit class method
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        print("id(self) in __new__", id(self))
        return self

    # instance method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("id(self) in __init__", id(self))


if __name__ == '__main__':
    h = Hoge()
    print(h)
