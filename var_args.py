# use keyword-only arguments to help ensure code clarity
def kwarg_only_func(arg1, arg2, *, flag=False, **kwargs):  #
    print(arg1, arg2, flag)


# kwarg_only_func(1, 2, True)  # NG
kwarg_only_func(1, 2, flag=True)


# kwarg_only_func(1, 2, 3, flag=True)  # NG


# var-args
def var_args(name, *args):
    print(name)
    print(args)  # tuple


var_args("hoge", None, 5, 3.0, "fefe", True)


# Keyword args
def var_args2(name, **kwargs):
    print(name)
    print(kwargs["desc"])
    print(kwargs)  # dict


var_args2("fuga", desc="description", feedback="feedback")


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


def pack_both(arg1=None, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)


pack_both("gege", "a", 4, fuga=5, fefe=False)
