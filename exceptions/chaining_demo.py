def func():
    raise ValueError('from func()')


# set __cause__ = None
def demo1():
    try:
        func()
    except ValueError:
        raise RuntimeError('from demo1()')


# set __cause__ = e
def demo2():
    try:
        func()
    except ValueError as e:
        raise RuntimeError('from demo2()') from e


# set __cause__ = None, and suppress chaining
def demo3():
    try:
        func()
    except ValueError:
        raise RuntimeError('from demo3()') from None


def run_demo(f):
    print('---', f.__name__)
    try:
        f()
    except Exception as e:
        print(e)
        print('__context__:', repr(e.__context__))
        print('__cause__:', repr(e.__cause__))

    print()


if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()

    run_demo(demo1)
    run_demo(demo2)
    run_demo(demo3)
