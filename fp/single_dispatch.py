# Generic function
# Overloading

from functools import singledispatch
from collections.abc import Sequence


@singledispatch
def fun(arg):
    return f'default: {arg}'


# Registering behaviors to correspond to each types

@fun.register(int)
def fun_int(arg):
    return f'int: {arg}'


@fun.register(list)
def fun_list(arg):
    return f'list: {arg}'


@fun.register(tuple)
def _(arg):
    return f'tuple: {arg}'


# @fun.register(str)
# def _(arg):
#     return 'str: {arg}'


@fun.register(Sequence)
def _(arg):
    return f'sequence: {arg}'


print(fun(3))
print(fun([5]))
print(fun((2,)))
print(fun('hoge'))
print(fun(object()))
