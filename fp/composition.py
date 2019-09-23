from functools import reduce, partial


def double(x):
    return x * 2


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def neg(x):
    return -x


def compose2(f, g):
    return lambda x: g(f(x))


inc_and_double = compose2(inc, double)
print(inc_and_double(10))

# nest
inc_double_and_dec = compose2(compose2(inc, double), dec)
print(inc_double_and_dec(10))


# reduce
def compose_n(*funcs):
    return reduce(compose2, funcs, lambda x: x)


# lambda
def compose(*funcs):
    return reduce(lambda f, g: lambda x: g(f(x)), funcs)  # initial omitted


inc_double_and_dec = compose_n(inc, double, dec)
print(inc_double_and_dec(10))
inc_double_and_dec = compose(inc, double, dec)
print(inc_double_and_dec(10))

# partial
pipeline = compose(partial(sub, y=4), neg)
print(pipeline(-6))
