# numbers: int, float
import math
import cmath
import sys
from decimal import Decimal, getcontext, FloatOperation
from fractions import Fraction

# int: unlimited precision signed integer
# very different from another languages
print(math.factorial(50))

print(0b10)
print(0o10)
print(0x10)

print(bin(42))
print(oct(42))
print(hex(42))
print(hex(42)[2:])
print(int('2a', base=16))
print(int('0o664', base=8))
print(int('0o664', base=0))
print(int('acghd', base=18))

print()

# float: IEEE754
# base2
# double precision (64bit) = 1: sign, 11: exponent, 52: fraction
# 53bit precision = 15-17 decimal precision

print(3e8)
print(1.616e-35)
print(100.616e-35)
print(float('NaN'))  # nan
print(float('Infinity'))  # inf
print(float('-Infinity'))  # -inf

print(sys.float_info)
print(sys.float_info.max)
print(sys.float_info.min)

# precision test
print(float(2**53))
print(float(2**53 + 1))
print(float(2**53 + 2))
print(float(2**53 + 3))
print(float(2**53 + 4))

print(0.8 - 0.7)

print(round(1.5))
print(round(2.5))  #
print(round(3.5))
print(round(2.675, 2))  #

print()

# Decimal: IEEE854
# 28 digits decimal precision by default
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
# d1 += 1.0  # NG

print(-7 % 3)  # => 2: -3 * 3 + 2
print(Decimal('-7') % Decimal('3'))  # => -1: -3 * 3 - 1
print(-7 // 3)  # => -3
print(Decimal('-7') // Decimal('3'))  # => -2


def is_odd(n):
    # return n % 2 == 1
    return n % 2 != 0  # Decimal(-1) % 2 = Decimal('-1')


print(is_odd(Decimal(-3)))

print(Decimal('0.81').sqrt())

print()

# Rational
# numerator / denominator
print(Fraction(2, 3))
print(Fraction(0.5))
print(Fraction(0.1))  #
print(Fraction(Decimal('0.1')))
print(Fraction('0.1'))
print(abs(Fraction('-0.1')))
print(math.floor(Fraction('4/3')))
print(round(Fraction('4/3')))
print(math.floor(Fraction('-4/3')))
print(round(Fraction('-4/3')))
print(Fraction('-7') % Fraction('3'))  # => 2: -3 * 3 + 2

# Complex
print(2j)
print(type(3 + 4j))
print(complex(-2, 3))
print(complex('-2+3j'))
# print(complex('-2 + 3j'))  # NG
c = 3 + 5j
print(c.real, c.imag)  # float
print(c.conjugate())
print(cmath.sqrt(-1))
print(cmath.phase(1 + 1j))  # x-axis: 1, y-axis: 1 => 0.785 rad (45°)
print(abs(1 + 1j))
print(abs(complex(0, -5)))
modulus, phase = cmath.polar(1 + 1j)
print(modulus, phase)
print(cmath.rect(modulus, phase))  # float
