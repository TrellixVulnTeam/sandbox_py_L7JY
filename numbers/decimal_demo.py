# Decimal: IEEE854
# 28 digits decimal precision by default
from decimal import Decimal, getcontext, FloatOperation

print(getcontext())

print(Decimal('0.9'))
print(Decimal(0.9))  # important
print(Decimal(0.8) == Decimal('0.8'))
print(Decimal('nan'))  # NaN
print(Decimal('inf'))  # Infinity
print(Decimal('-inf'))  # -Infinity
print(int(Decimal(5)))
print(float(Decimal(5)))

print(Decimal('0.8') - Decimal('0.7'))
print(Decimal(0.8) - Decimal(0.7))

print(abs(Decimal('-1.00')))
print(round(Decimal('1.2345'), 2))

print(round(2.675, 2))  # *
print(round(Decimal('2.675'), 2))  # precise

# attention
print(Decimal('1'))
print(Decimal('1.0'))
print(Decimal('1.00'))
print(Decimal('1.00') == Decimal(1))  # True

getcontext().traps[FloatOperation] = True
# print(Decimal(0.7))  # NG
getcontext().traps[FloatOperation] = False

getcontext().prec = 6
d1 = Decimal('1.234567')
print(d1)
d1 += Decimal(1)
print(d1)
d1 += 1
print(d1)
# d1 += 1.0  # float NG

# dividend % divisor
print(-7 % 3)  # => 2: -3 * 3 + 2
print(Decimal('-7') % Decimal('3'))  # => -1: -3 * 3 - 1

# dividend // divisor
print(-7 // 3)  # => -3
print(Decimal('-7') // Decimal('3'))  # => -2


def is_odd(n):
    # return n % 2 == 1
    return n % 2 != 0  # Decimal(-1) % 2 = Decimal('-1')


print(is_odd(Decimal(-3)))

# math functions don't work with Decimal
# use Decimal methods
print(Decimal('0.81').sqrt())
