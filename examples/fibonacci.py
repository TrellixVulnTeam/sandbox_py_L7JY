# DP
def fib(n):
    if n < 2:
        return n

    a, b = 0, 1
    # for _ in range(2, n + 1):
    for _ in range(n - 1):
        a, b = b, a + b
    return b


for x in range(6):
    print(fib(x))


# Recursive
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


for x in range(6):
    print(fib(x))


# Generator
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for x in fib(6):
    print(x)
