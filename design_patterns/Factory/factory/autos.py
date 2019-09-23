import abc


class AbsAuto(metaclass=abc.ABCMeta):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class ChevyVolt(AbsAuto):
    def start(self):
        print('%s running with shocking power!' % self.name)

    def stop(self):
        print('%s shutting down.' % self.name)


class FordFocus(AbsAuto):
    def start(self):
        print('%s running cooly!' % self.name)

    def stop(self):
        print('%s shutting down.' % self.name)


class JeepSahara(AbsAuto):
    def __init__(self, name):
        self._name = name

    def start(self):
        print('%s running ruggedly.' % self.name)

    def stop(self):
        print('%s shutting down.' % self.name)


class NullCar(AbsAuto):
    def start(self):
        print('Unknown car "%s".' % self.name)

    def stop(self):
        pass
