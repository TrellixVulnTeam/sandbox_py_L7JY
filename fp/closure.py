# closure: Function factory
def closure(x):
    def _(y):
        return x + y

    return _


print(closure.__name__)
print(closure(0).__closure__)
print(closure(1)(1))


def enclosing():
    x = 0

    def local_func():
        print(x)

    return local_func


lf = enclosing()
lf()
lf()


def enclosing():
    x = 0

    def local_func():
        nonlocal x
        x += 1
        print(x)

    return local_func


lf = enclosing()
lf()
lf()

print()

s = "s@global"


def func():
    def inner(): return s

    s = "s@inner()"  # 位置に注目
    return inner


print(func()())
print(s)
