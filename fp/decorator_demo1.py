# decorator, closure
from functools import wraps, update_wrapper


# basic decorator
def logme(func):
    def wrapper(*args, **kwargs):
        print("Before func() call")
        print(f"Called: '{func.__name__}': args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)  # call
        print("After func() call")
        return result

    return wrapper


@logme
def fuga(msg=None, **kwargs):
    print(msg, kwargs)


fuga('FUGA', kwarg2=2)

print('---')


# with decorator args
def decorator_with_args(*dargs, **dkwargs):  # decorator factory, just return the decorator
    def decorator(f):  # the actual decorator
        def wrapper(*args, **kwargs):
            print("Decorator arguments:", dargs, dkwargs)
            print("f() arguments:", args, kwargs)
            return f(*dargs, **dkwargs)

        return wrapper

    return decorator


@decorator_with_args("hello", "world", number=42)
def say_hello(*args, **kwargs):
    print('say_hello arguments:', args, kwargs)


say_hello("hoge", "fuga", number=11)

print('---')


# Callable
class CallCount:
    def __init__(self, func):  #
        update_wrapper(self, func)  # pretend
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello, {}'.format(name))


@CallCount
def hello2(name):
    print('Hello, {}'.format(name))


hello('Hoge')
hello('Fuga')
hello('FeFe')
print(hello.count)

hello2('Hoge')
hello2('Fuga')
print(hello2.count)

print('---')


# multiple decorators order
def surround_tag(tag):
    def decorator(fn):
        @wraps(fn)
        def _(html):
            print(tag)
            return f"<{tag}>{fn(html)}</{tag}>"
            # return fn(f"<{tag}>{html}</{tag}>")  # reverse order

        return _

    return decorator


@surround_tag("b")
@surround_tag("i")
def hello(msg):
    return msg


print(hello("Hello World!"))


def hello2(msg):
    return msg


print(
    surround_tag("b")(
        surround_tag("i")(
            hello2
        )
    )("Hello World!")
)

print('---')


# function metadata
def noop_bare(f):
    """bare wrapper"""

    def wrapper():
        return f()

    # preserve metadata
    # wrapper.__name__ = f.__name__
    # wrapper.__doc__ = f.__doc__
    return wrapper


def noop(f):
    """preserve metadata by functools.wraps"""

    @wraps(f)
    def wrapper():
        return f()

    return wrapper


@noop_bare
def hello1():
    """docstring of hello1()"""
    print('Hello, world!')


print(f"__name__: {hello1.__name__}, __doc__: {hello1.__doc__}")


@noop
def hello2():
    """docstring of hello2()"""
    print('Hello, world!')


print(f"__name__: {hello2.__name__}, __doc__: {hello2.__doc__}")

print('---')


# decorator args
def munch(start, end):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_string = ''
            result = func(*args, **kwargs)
            for index, char in enumerate(result):
                c = '_' if start <= index < end else char
                new_string += c
            return new_string

        return wrapper

    return decorator


@munch(4, 7)
def hoge():
    return 'HogeHoge'


print(hoge())

print('---')


# decorator args
def check_non_negative(index):
    def validator(f):
        @wraps(f)
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(f"Argument {index} must be non-negative.")
            return f(*args)

        return wrap

    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size


print(create_list('a', 3))
print(create_list(123, -6))
