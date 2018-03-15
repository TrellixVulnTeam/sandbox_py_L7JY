#!/usr/bin/env python3

from decimal import Decimal


def calc(a, b):
    x = a + a + a - b
    print('x is {}'.format(x))
    print(type(x))


calc(0.10, 0.30)
calc(Decimal('0.10'), Decimal('0.30'))
