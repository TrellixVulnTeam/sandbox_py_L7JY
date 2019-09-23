# Memoize using Proxy pattern(Virtual Proxy)
import time


class RawCalculator(object):
    """  Don't touch me """

    def fib(self, n):
        if n < 2:
            return 1
        return self.fib(n - 2) + self.fib(n - 1)


def memoize(f):
    cache = {}

    def memoized(*args):
        key = (f.__name__, args)
        if key not in cache:
            cache[key] = f(*args)
        return cache[key]

    return memoized


class CalculatorProxy(object):
    def __init__(self, target):
        self.target = target
        # fib = getattr(self.target, 'fib')
        fib = self.target.fib
        setattr(self.target, 'fib', memoize(fib))  # memoizeを機能させるためにtargetのメソッドを上書きする必要がある

    def __getattr__(self, name):
        return getattr(self.target, name)


def measure(f):
    def _(n):
        start_time = time.time()
        res = f(n)
        end_time = time.time()
        print('result: {}, elapsed: {}'.format(res, end_time - start_time))
        return f

    return _


if __name__ == "__main__":
    calculator = CalculatorProxy(RawCalculator())
    measure(calculator.fib)(33)  # memoizeとは違い、直接呼び出しても良い

    raw_calculator = RawCalculator()
    measure(raw_calculator.fib)(33)
