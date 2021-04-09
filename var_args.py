# Positional args
def var_args(name, *args):
    print(name)
    print(args)  # tuple


var_args("hoge", None, 5, 3.0, "fefe", True)
var_args("hoge", 111)


# Keyword args
def var_args2(name, **kwargs):
    print(name)
    print(kwargs["desc"])
    print(kwargs)  # dict


var_args2("fuga", desc="description", feedback="feedback")


# Mixed positional args and keyword args
def var_args3(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1, arg2)
    print(args)
    print(kwarg1, kwarg2)
    print(kwargs)


var_args3(1, 2, 3, 4, kwarg1=5, kwarg2=6, hoge=7, fuga=8)


# Keyword-only args
def var_arg4(arg1, arg2, *, kwarg1=0, **kwargs):
    print(arg1, arg2, kwarg1, kwargs)


# var_arg4(1, 2, 3, hoge=4)  # NG
var_arg4(1, 2, kwarg1=3, hoge=4)


# Positional-only args (Python3.8)
def var_arg5(x, /):
    print(x)


# var_arg5(x=100)  # NG
var_arg5(100)

# Positional-only args example in PSL
# print([x for x in range(start=1, stop=10, step=2)])  # NG
print([x for x in range(1, 10, 2)])


# packing, unpacking
def pack_args(*args):
    print(args)


pack_args("a", 4, True, )
pack_args(*("a", 4, True,))
pack_args(*["a", 4, True, ])
pack_args(*{"a", 4, True, })  # unordered


def pack_kwargs(**kwargs):
    print(kwargs)


pack_kwargs(hoge=2, fuga=5, fefe=False)
pack_kwargs(**{"hoge": 2, "fuga": 5, "fefe": False})


def pack_mixed(arg1=None, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)


a = ["gege", "a", 4, ]
k = {"fuga": 5, "fefe": False}
l = {"arg1": 1, "arg2": 2, "arg3": 3, "fuga": 5, "fefe": False}
pack_mixed(*a, **k)
pack_mixed(**l)

print()

print('--- pitfall of mutable default arguments')


def add_spam(menu=[]):
    menu.append('spam')
    return menu


print(add_spam(['bacon', 'eggs']))
print(add_spam())
print(add_spam())

print()

import time


def show_default(arg=time.ctime()):  # run only once at definition
    print(arg)


show_default()
time.sleep(1)
show_default()
time.sleep(1)
show_default()
