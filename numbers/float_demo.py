# float: IEEE754
# base2
# double precision (64bit) = 1: sign, 11: exponent, 52: fraction
# 53bit precision = 15-17 decimal precision
import sys

print(sys.float_info)
print(sys.float_info.max)
print(sys.float_info.min)

print(3e8)
print(1.616e-35)
print(100.616e-35)
print(float('NaN'))  # nan
print(float('Infinity'))  # inf
print(float('-Infinity'))  # -inf

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
