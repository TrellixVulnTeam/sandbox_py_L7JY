from fractions import Fraction


def mixed_numeral(vulgar):
    try:  # optimistic
        integer = vulgar.numerator // vulgar.denominator
        fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
                            vulgar.denominator)
        return integer, fraction
    except AttributeError as e:
        raise TypeError("{} is not a rational number".format(vulgar)) from e


if __name__ == '__main__':
    print(mixed_numeral(5))
    print(mixed_numeral(Fraction('11/10')))
    print(mixed_numeral(Fraction('17/3')))
    print(mixed_numeral(1.7))
