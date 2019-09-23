import abc


class AbsCar(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def description(self):
        pass

    @property
    @abc.abstractmethod
    def cost(self):
        pass


class Economy(AbsCar):
    @property
    def description(self):
        return 'Economy'

    @property
    def cost(self):
        return 12000.00


class Economy4CylWhiteVinyl(Economy):
    @property
    def description(self):
        return 'Economy, white, 4 cylinder, vinyl upholstery'

    @property
    def cost(self):
        return 12000.00


class Economy6CylWhiteVinyl(Economy):
    @property
    def description(self):
        return 'Economy, 6 cylinder, white, vinyl upholstery'

    @property
    def cost(self):
        return 13500.00
