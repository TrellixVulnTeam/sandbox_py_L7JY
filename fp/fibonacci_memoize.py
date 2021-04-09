# Memoize using Proxy pattern(Virtual Proxy)
from functools import wraps, lru_cache
from time import perf_counter


def measure(func):
    total = 0  # scope: measure()

    @wraps(func)
    def _(n):
        nonlocal total
        start = perf_counter()
        result = func(n)
        end = perf_counter()
        duration = end - start  # scope: _()
        total += duration
        print(f'{func.__name__}({n}) = {result} -> {duration:.8f}, Total: {total:.8f}')
        return result

    return _


# closure
def memoize(f):
    cache = {}

    @wraps(f)
    def memoized(*args):
        key = (f.__name__, args)  #
        if key not in cache:
            cache[key] = f(*args)
        return cache[key]

    return memoized


# Recursive
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@memoize
def fib2(n):
    return n if n < 2 else fib2(n - 1) + fib2(n - 2)


@lru_cache(maxsize=None)
def fib3(n):
    return n if n < 2 else fib3(n - 1) + fib3(n - 2)


if __name__ == '__main__':
    measure(fib)(33)
    measure(fib2)(33)
    measure(fib3)(33)

    # measure(memoize(fib))(33)  # NG
    fib = memoize(fib)  # 必ず同じ名前で上書きする
    measure(fib)(33)

    fib = lru_cache(maxsize=None)(fib)
    measure(fib)(33)
