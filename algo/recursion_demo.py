# recursion demo
# RecursionError (Stack overflow)


def countdown(x):
    if x == 0:  # breaking condition
        print("Done!")
        return
    else:
        print("before:", x)
        countdown(x - 1)  # recursion
        print("after:", x)


def power(x, n):
    """very basic algorithm"""
    if n < 0:
        return power(1 / x, -n)
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x, n - 1)


if __name__ == '__main__':
    countdown(5)

    print()
    print(power(2, 3))
    print(power(2, 4))
    print(power(2, -2))
    print(power(2, -3))
