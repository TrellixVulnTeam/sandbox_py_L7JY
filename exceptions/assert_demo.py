"""
default: assert stmt will be executed

__debug__ == False
python -O hoge.py
"""


def main():
    assert False, "Assertion!"


def bad_demo(x):
    assert x < 10, "x cannot be over 10."


def good_demo(x):
    if x > 10:
        raise ValueError("x cannot be over 10.")


if __name__ == '__main__':
    print(__debug__)
    # main()
    print()
    # bad_demo(11)
    good_demo(11)
