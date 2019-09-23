from collections.abc import Iterable
from match import Match


class Hoge:
    pass


class Item:
    pass


def demo1(arg):
    with Match(arg) as m:
        # ヒットしたところで抜ける
        m(42) >> (lambda _: 'The Answer')
        (m(41) | m(43)) >> (lambda matched: 'Matched value %s' % matched)
        m(lambda x: x % 2 == 0) >> (lambda matched: '%s is even' % matched)  # number以外で例外
        m(int) >> (lambda matched: '%d is an integer' % matched)
        m(...) >> (lambda unmatched: '%s was not matched' % unmatched)
        print(m.result)
        # catch missing match patterns


def demo2(tup):
    """
    Validation using Match demo
    """

    def isint(x):
        return isinstance(x, int)

    def ishoge(x):
        return isinstance(x, Hoge)

    def isiterable(x):
        return isinstance(x, Iterable)

    def allitems(x):
        return isiterable(x) and all(isinstance(e, Item) for e in x)

    with Match(tup) as m:
        m((4, ..., ...)) >> (lambda t: 'Matched tuple: %s' % repr(t))
        m((isint, ishoge, allitems)) >> (lambda t: 'Validated tuple: %s' % repr(t))
        m(tuple) >> (lambda t: 'No match for tuple: %s' % repr(t))
        m(...) >> (lambda t: 'Not tuple: %s' % repr(t))
        print(m.result)


def demo3(tup):
    """
    Validation using Match demo
        先抜けなので、詳細度の低いものからMatchingを行うようにする。
    """

    def error(msg):
        raise ValueError(msg)

    def nottuple(x):
        return not isinstance(x, tuple)

    def notint(x):
        return not isinstance(x, int)

    def nothoge(x):
        return not isinstance(x, Hoge)

    def notiterable(x):
        return not isinstance(x, Iterable)

    def notallitems(x):
        return notiterable(x) or not all(isinstance(e, Item) for e in x)

    # TODO: lambdaをerror()に置き換えるとおかしくなる
    with Match(tup) as m:
        m(nottuple) >> (lambda t: 'Not tuple: %s' % repr(m.match))
        m((notint, ..., ...)) >> (lambda t: '1st arg must be int: %s' % repr(m.match))
        m((..., nothoge, ...)) >> (lambda t: '2nd arg must be Hoge class: %s' % repr(m.match))
        m((..., ..., notallitems)) >> (
            lambda t: '3rd arg must be all Item class: %s' % repr(m.match)
        )
        m(...) >> (lambda x: 'Good!')
        print(m.result)


if __name__ == '__main__':
    demo1(41)
    demo1(42)
    demo1(5)
    demo1(2)
    demo1(3.14159265)

    print()

    values = [
        'hoge',
        ('hoge', 3, 2),
        (4, 'xxx', 5.5),
        (1, 3, 5),
        (8, Hoge(), [Item(), object()]),
        (5, Hoge(), [Item(), Item()]),
    ]

    for i in values:
        demo2(i)

    print()

    for i in values:
        try:
            demo3(i)
        except ValueError as e:
            print(e)
