# recursion demo
# RecursionError (Stack overflow)
import sys


def s(n):
    if n == 0:
        return n
    else:
        return n + s(n - 1)


# tail recursion optimization: not supported in python
def s2(n, acc=0):
    if n == 0:
        return acc
    else:
        return s2(n - 1, acc + n)


if __name__ == '__main__':
    print(sys.getrecursionlimit())
    print(s(997))
    print(s2(997))
    # print(s(998))
    print(s2(998))
