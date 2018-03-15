def var_args(name, *args):
    print(name)
    print(args)  # tuple


var_args("hoge", None, 5, 3.0, "fefe", True)


# Key Word args
def var_args2(name, **kwargs):
    print(name)
    print(kwargs["desc"])
    print(kwargs)  # dict


var_args2("fuga", desc="description", feedback="feedback")
