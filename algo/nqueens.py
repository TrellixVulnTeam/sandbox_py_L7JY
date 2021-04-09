from itertools import permutations


def nqueens(n):
    """ Simple but not efficient """
    cols = range(n)
    return [vec for vec in permutations(cols)
            if (n == len(set(vec[i] + i for i in cols))
                == len(set(vec[i] - i for i in cols)))]


def nqueens2(n):
    """ backtracking """
    vectors = []

    def algo(r, n, p):
        s = len(p)
        cols = range(s)
        if (s == len(set(p[i] + i for i in cols))
                == len(set(p[i] - i for i in cols))):
            if r == n:
                vectors.append(p)
                return
            for c in set(range(n)) - set(p):
                algo(r + 1, n, p + [c])

    algo(0, n, [])

    return vectors


def measure(f):
    def _(n):
        from time import time
        start = time()
        res = f(n)
        print(time() - start)
        return res

    return _


if __name__ == '__main__':
    sols = measure(nqueens)(10)
    print(len(sols))

    sols = measure(nqueens2)(10)
    print(len(sols))
