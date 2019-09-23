# Memoize using Proxy pattern(Virtual Proxy)
import time


# Recursive
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def memoize(f):
    cache = {}

    def memoized(*args):
        key = (f.__name__, args)
        if key not in cache:
            cache[key] = f(*args)
        return cache[key]

    return memoized


def measure(f):
    def _(n):
        start_time = time.time()
        res = f(n)
        end_time = time.time()
        print('result: {}, elapsed: {}'.format(res, end_time - start_time))
        return f

    return _


if __name__ == '__main__':
    measure(fib)(33)

    # measure(memoize(fib))(33)  # NG
    # hoge = memoize(fib)  # 別名はNG
    # measure(hoge)(33)
    fib = memoize(fib)  # 必ず同じ名前で上書きする
    measure(fib)(33)
