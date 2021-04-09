# Fraction (Rational)
import math
from decimal import Decimal
from fractions import Fraction

# numerator / denominator
two_third = Fraction(2, 3)
print(two_third)
print(two_third.numerator)
print(two_third.denominator)

print(Fraction(0.5))
print(Fraction(0.1))  # !!
print(Fraction(Decimal('0.1')))
print(Fraction('0.1'))
print(abs(Fraction('-0.1')))
print(math.floor(Fraction('4/3')))
print(round(Fraction('4/3')))
print(math.floor(Fraction('-4/3')))
print(round(Fraction('-4/3')))

print(Fraction('-7') % Fraction('3'))  # => 2: -3 * 3 + 2
print(Fraction(2, 3) + Fraction(4, 5))
print(Fraction(2, 3) - Fraction(4, 5))
print(Fraction(2, 3) * Fraction(4, 5))
print(Fraction(2, 3) / Fraction(4, 5))
print(Fraction(2, 3) // Fraction(4, 5))
print(Fraction(2, 3) % Fraction(4, 5))
