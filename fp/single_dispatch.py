# Generic function
# Overloading

from functools import singledispatch


@singledispatch
def fun(arg):
    return 'default'


# Registering behaviors to correspond to each types

@fun.register(int)
def fun_int(arg):
    return 'int'


@fun.register(list)
def fun_list(arg):
    return 'list'


print(fun(3))
print(fun([]))
print(fun('hoge'))  # str type is not registered.

assert fun_int('dummy') == 'int'
assert fun_list('dummy') == 'list'
assert fun(object()) == 'default'  # Using 'instance of object' to test the default behavior.
