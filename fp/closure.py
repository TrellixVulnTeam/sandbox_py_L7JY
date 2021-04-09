# closure: Function factory


def enclosing():
    x = "closed"

    def local_func():
        return x, y

    y = "over"

    return local_func


lf = enclosing()
print(lf.__closure__)  # recorded objects from the enclosing scope
print(lf())

print()


def enclosing():
    x = 0

    def local_func():
        nonlocal x
        x += 1
        return x

    return local_func


lf = enclosing()
print(lf())
print(lf())

print()


def enclosing(x):
    def _(y):
        return x + y

    return _


print(enclosing(0).__closure__)
print(enclosing("").__closure__)
print(enclosing(1)(1))
print(enclosing(4)(2))
print(enclosing("abc")("xyz"))
