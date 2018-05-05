class A:
    f = "A"


class B:
    f = "B"


class Demo(A, B):
    pass


print(Demo().f)
