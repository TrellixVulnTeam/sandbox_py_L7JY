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


big_sum()

print('---')


def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner(*args, **kwargs):
        logging.debug("Called: {} with args: {} and kwargs: {}"
                      .format(func.__name__, args, kwargs))
        return func(*args, **kwargs)  # call

    inner.__doc__ = func.__doc__
    inner.__name__ = func.__name__
    return inner


def logme_by_wraps(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
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


@logme
def sub2(x, y, switch=False):
    """
    Returns the difference between two numbers
    """
    return x - y if not switch else y - x


print(sub2(5, 2, True))
print(sub2(5, 2, switch=True))

help(sub2)
print(sub2.__doc__)
print(sub2.__name__)

print('---')


@logme_by_wraps
def sub3(x, y, switch=False):
    """
    Returns the difference between two numbers
    """
    return x - y if not switch else y - x


print(sub3(5, 2, True))
print(sub3(5, 2, switch=True))

help(sub3)
print(sub3.__doc__)
print(sub3.__name__)

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


fefe('fefe')
