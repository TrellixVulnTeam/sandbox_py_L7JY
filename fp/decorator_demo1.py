# decorator, closure
from functools import wraps
import logging

logging.basicConfig(level=logging.DEBUG)


# basic decorator
def logme(func):
    def inner(*args, **kwargs):
        logging.debug("Called: {} with args: {} and kwargs: {}"
                      .format(func.__name__, args, kwargs))
        return func(*args, **kwargs)  # call

    return inner


@logme
def fuga(msg=None):
    print(msg)


fuga('FUGA')


def hoge(msg=None):
    print(msg)


logme(hoge)('HOGE')

print('---')


# with decorator args
def decorator_with_args(*dargs):
    def wrap(f):
        print("Inside wrap()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", *dargs)
            f(*args)
            print("After f(*args)")

        return wrapped_f

    return wrap


@decorator_with_args("hello", "world", 42)
def say_hello(*args):
    print('say_hello arguments:', *args)


say_hello("say", "hello", "arguments")

print()


def say_hello2(*args):
    print('say_hello2 arguments:', *args)


decorator_with_args("hoge", "fuga")(say_hello2)("say", "hello", "arguments")

print('---')


# Callable
class CallCount:
    def __init__(self, f):  #
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount  # CallCount(f)
def hello(name):
    print('Hello, {}'.format(name))


hello('Hoge')
hello('Fuga')
hello('FeFe')
print(hello.count)

print('---')


# decorator order
def dec1(func):
    def wrapped(msg):
        return func('dec1({})'.format(msg))

    return wrapped


def dec2(func):
    def wrapped(msg):
        return func('dec2({})'.format(msg))

    return wrapped


@dec1
@dec2
def fefe(msg):
    print(msg)


fefe('Hello!')  # dec2(dec1('Hello!'))

print('---')


def noop_bare(f):
    """bare wrapper"""

    def wrapped():
        return f()

    # preserve metadata
    # wrapped.__doc__ = f.__doc__
    # wrapped.__name__ = f.__name__
    return wrapped


def noop(f):
    """preserve metadata by functools.wraps"""

    @wraps(f)
    def wrapped():
        return f()

    return wrapped


@noop_bare
def hello1():
    """docstring of hello1()"""
    print('Hello, world!')


help(hello1)


@noop
def hello2():
    """docstring of hello2()"""
    print('Hello, world!')


help(hello2)

print('---')


# decorator args
def check_non_negative(index):  # decorator factory, just return the decorator
    def validator(f):  # the actual decorator
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non-negative.'.format(index))
            return f(*args)

        return wrap

    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size


print(create_list('a', 3))
print(create_list(123, -6))
