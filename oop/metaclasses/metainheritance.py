class MetaA(type):
    def __new__(mcs, *args, **kwargs):
        print("MetaA.__new__")
        return super().__new__(mcs, *args, **kwargs)

    def __init__(cls, name, bases, namespace):
        print("MetaA.__init__")
        super().__init__(name, bases, namespace)


class MetaB(type):
    def __new__(mcs, *args, **kwargs):
        print("MetaB.__new__")
        return super().__new__(mcs, *args, **kwargs)

    def __init__(cls, name, bases, namespace):
        print("MetaB.__init__")
        super().__init__(name, bases, namespace)


class MetaC(MetaA, MetaB):
    """
    metaclass mixin
    いつもうまくmixinできるとは限らない。
    """
    pass


print('*** A definition ***')


class A(metaclass=MetaA):
    pass


print('*** B definition ***')


class B(metaclass=MetaB):
    pass


print('*** D definition ***')


class D(A):
    pass


print('*** C definition ***')


# metaclass conflict
# class C(A, B):
#     pass


class C(A, B, metaclass=MetaC):
    pass


if __name__ == '__main__':
    print()
    print('*** __main__ ***')
    print(type(MetaA))
    print(type(D))
    print(type(C))
