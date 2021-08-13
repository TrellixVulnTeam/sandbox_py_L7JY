# for-else demo

# dividend: 被除数
# divisor: 除数
# quantifier: 商
# remainder: 剰余


def for_else(items, divisor):
    for item in items:
        if item % divisor == 0:
            dividend = item
            break
    else:  # nobreak
        dividend = 'NONE'
    print("{items} contains {dividend} which is a multiple of {divisor}".format(
        **locals()))


# using function instead of for-else
def has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    return 'NONE'


def by_func(items, divisor):
    dividend = has_divisible(items, divisor)
    print("{items} contains {dividend} which is a multiple of {divisor}".format(
        **locals()))


if __name__ == '__main__':
    items = [2, 25, 9, 24, 37, 28, 14]
    items_n = [2, 25, 9, 37, 28, 14]
    divisor = 12

    for_else(items, divisor)
    for_else(items_n, divisor)
    by_func(items, divisor)
    by_func(items_n, divisor)
