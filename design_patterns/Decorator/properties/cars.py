import abc


class AbsCar(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def description(self):
        pass

    @property
    @abc.abstractmethod
    def engine(self):
        pass

    @property
    @abc.abstractmethod
    def paint(self):
        pass

    @property
    @abc.abstractmethod
    def upholstery(self):
        pass

    def cost(self):
        cost = 0.00
        if self.engine == '4 cyl':
            cost += 0.00
        elif self.engine == '6 cyl':
            cost += 1500.00
        if self.paint == 'white':
            cost += 0.00
        elif self.paint == 'black':
            cost += 1000.00
        elif self.paint == 'red':
            cost += 2000.00
        if self.upholstery == 'vinyl':
            cost += 0.00
        elif self.upholstery == 'leather':
            cost += 2000.00
        return cost


class Economy(AbsCar):
    def __init__(self, engine, paint, upholstery):
        self._engine = engine
        self._paint = paint
        self._upholstery = upholstery

    @property
    def description(self):
        return 'Economy'

    @property
    def engine(self):
        return self._engine

    @property
    def paint(self):
        return self._paint

    @property
    def upholstery(self):
        return self._upholstery

    @property
    def cost(self):
        return 12000.00 + super().cost()
