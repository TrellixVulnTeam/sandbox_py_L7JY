class Resistor1:

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts


# no dynamic feature
class Resistor2:
    __slots__ = ['resistance_ohms', 'tolerance_percent', 'power_watts']

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts


if __name__ == '__main__':
    import sys

    r1 = Resistor1(10, 5, 0.25)
    print(sys.getsizeof(r1))
    print(sys.getsizeof(r1) + sys.getsizeof(r1.__dict__))
    r1.cost_dollars = 0.02

    r2 = Resistor2(10, 5, 0.25)
    print(sys.getsizeof(r2))  # no __dict__
    # r2.cost_dollars = 0.02  # NG

    print()
    print(dir(r1))
    print(dir(r2))
    print(set(dir(r1)) - set(dir(r2)))
