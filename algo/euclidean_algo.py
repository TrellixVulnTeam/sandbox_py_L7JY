"""
Euclidean algorithm
GCD: Great Common Divisor
"""


def gcd(m, n, verbose=True):
    while n != 0:
        r = m % n
        if verbose:
            print(f'{m} % {n} = {r}')
        m, n = n, r

    if verbose:
        print(f'GCD is {m}')
        print()

    return m


if __name__ == '__main__':
    gcd(20, 8)
    gcd(8, 20)
    gcd(0, 10)
    gcd(60, 96)
    gcd(150, 304)
    gcd(12707, 12319)
