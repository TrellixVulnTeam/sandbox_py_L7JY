from cars import AbsCar


class AbsDecorator(AbsCar):
    def __init__(self, car):
        self._car = car

    @property
    def car(self):
        return self._car


class Black(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', midnight black'

    @property
    def cost(self):
        return self.car.cost + 1800.00


class Inline4Cyl(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', inline 4 cylinder'

    @property
    def cost(self):
        return self.car.cost + 500.00


class Leather(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', top-grain leather'

    @property
    def cost(self):
        return self.car.cost + 2700.00


class Red(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', Ferarri red'

    @property
    def cost(self):
        return self.car.cost + 1200.00


class V6(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', V6'

    @property
    def cost(self):
        return self.car.cost + 1200.00


class Vinyl(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', vinyl upholstery'

    @property
    def cost(self):
        return self.car.cost + 500.00


class White(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', white'

    @property
    def cost(self):
        return self.car.cost + 800.00
