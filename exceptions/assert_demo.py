"""
default: assert stmt will be executed

__debug__ == False
python -O hoge.py
"""


def bad_demo(x):
    # Do not use assert for like input validation
    assert x < 10, "x cannot be over 10."


def good_demo(x):
    if x > 10:
        raise ValueError("x cannot be over 10.")


def dangerous():
    # always True because of the assertion against non-empty tuple
    assert (1 == 2, 'This should fail')


if __name__ == '__main__':
    print(__debug__)
    print()
    # bad_demo(11)
    # good_demo(11)
    dangerous()
