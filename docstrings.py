""" Demonstrate the use of function docstrings and doctest

Doctest (if successful, return nothing)
python -m doctest docstrings.py
"""


def func(arg1, arg2=None):
    """func(arg1, arg2=None) --> Doesn't really do anything special.

    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: the second argument. Defaults to None. Whatever makes you happy.
    """
    print(arg1, arg2)


def add(x, y):
    """Add 2 items
    :param: x
    :param: y
    :return: x + y

    >>> add(2, 2)
    4
    >>> add("hoge", "fuga")
    'hogefuga'
    """
    return x + y


if __name__ == "__main__":
    # print(func.__doc__)
    help(func)
    help(add)

    # doctest from code
    import doctest

    doctest.testmod()
