# complex impedance plane
import cmath
import math


def inductive(ohms):
    return complex(0.0, ohms)


def capactive(ohms):
    return complex(0.0, -ohms)


def resistive(ohms):
    return complex(ohms)


def impedance(components):
    z = sum(components)
    return z


if __name__ == '__main__':
    i = impedance([inductive(10), resistive(10), capactive(5)])
    print(i)
    phase = cmath.phase(i)
    print(phase)
    dphase = math.degrees(phase)
    print(dphase)
