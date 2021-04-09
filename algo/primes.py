# Test for prime number


def is_prime(n):
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += 1
    return True


print([x for x in range(1, 500) if is_prime(x)])
