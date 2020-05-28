# pytest assertion demo
from pytest import approx, raises


def test1():
    assert (0.1 + 0.2) == 0.3


def test2():
    assert (0.1 + 0.2) == approx(0.3)


def raisesValueError():
    raise ValueError


def test_exception():
    with raises(ValueError):
        raisesValueError()
