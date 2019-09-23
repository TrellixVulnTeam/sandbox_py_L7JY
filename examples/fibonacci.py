# Dynamic Programming
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a

print([fib(x) for x in range(6)])


# Recursive
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


print([fib(x) for x in range(6)])


# Generator
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print([x for x in fib(6)])
