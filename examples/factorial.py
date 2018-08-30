# DP
def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


for x in range(6):
    print(factorial(x))


# Recursive
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


for x in range(6):
    print(factorial(x))


# Generator
def factorial(n):
    a = 1
    for i in range(1, n + 1):
        yield a
        a *= i


for x in factorial(6):
    print(x)
