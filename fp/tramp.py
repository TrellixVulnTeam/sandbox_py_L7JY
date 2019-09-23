import types


def tramp(gen, *args, **kwargs):
    """
    Trampoline
    """
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g
