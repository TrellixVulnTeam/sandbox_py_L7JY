# Proxy pattern using __getattribute__, __setattr__


class LoggingProxy:

    def __init__(self, target):
        super().__setattr__('target', target)

    def __getattribute__(self, name):  # all attributes access intercepted
        target = super().__getattribute__('target')

        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        else:
            print("Retrieved attribute {!r} = {!r} from {!r}".format(name, value, target))
            return value

    def __setattr__(self, name, value):
        target = super().__getattribute__('target')

        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target))
        else:
            print("Set attribute {!r} = {!r} on {!r}".format(name, value, target))

    # def __repr__(self):
    #     target = super().__getattribute__('target')
    #     repr_callable = getattr(target, '__repr__')
    #     return repr_callable()


if __name__ == '__main__':
    from vector import ColoredVector

    cv = ColoredVector(red=23, green=44, blue=238, p=9, q=14)
    cw = LoggingProxy(cv)
    print(cw.p)
    print(cw.red)
    cw.red = 5
    print(cw.red)
    # cw.p = 19  # rejected by the target object

    print()
    print(cw.__repr__())  # len, iter, and so on
    print(repr(cw))  # bypass __getattribute__
