# decorator, closure
from functools import wraps
import time


def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        # print(f'Elapsed time: {(t2 - t1) * 1000} ms')
        print('Elapsed time: {} ms'.format((t2 - t1) * 1000))

    return wrapper  # closure ref


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 1000)):
        num_list.append(num)
    # print(f'Big sum: {sum(num_list)}')
    print('Big sum: {}'.format(sum(num_list)))


big_sum()  # elapsed_time(big_sum)()

print('---')


def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner(*args, **kwargs):
        logging.debug("Called: {} with args: {} and kwargs: {}"
                      .format(func.__name__, args, kwargs))
        return func(*args, **kwargs)  # call

    return inner


def hoge(msg=None):
    print(msg)


logme(hoge)('HOGE')


@logme
def fuga(msg=None):
    print(msg)


fuga('FUGA')

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
    def wrapper(msg):
        return func('dec1({})'.format(msg))

    return wrapper


def dec2(func):
    def wrapper(msg):
        return func('dec2({})'.format(msg))

    return wrapper


@dec1
@dec2
def fefe(msg):
    print(msg)


fefe('fefe')  # dec2(dec1(fefe('fefe')))

print('---')


# functools.wraps usage
def noop_bare(f):
    def wrapper():
        return f()

    # preserve metadata
    # wrapper.__doc__ = f.__doc__
    # wrapper.__name__ = f.__name__
    return wrapper


def noop(f):
    @wraps(f)  # preserve metadata by functools.wraps
    def wrapper():
        return f()

    return wrapper


@noop_bare
def hello1():
    """ docstring of hello1()"""
    print('Hello, world!')


help(hello1)


@noop
def hello2():
    """ docstring of hello2()"""
    print('Hello, world!')


help(hello2)

print('---')


def check_non_negative(index):  # non decorator, just return the callable
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
