#!/usr/bin/env python3


def factorial(n):
    fac = 1
    for x in range(1, n + 1):
        fac = fac * x
    return fac


print(factorial(0))
print(factorial(5))


# Recursive
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


print(factorial(0))
print(factorial(5))
