import abc


class AbsAuto(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class ChevyVolt(AbsAuto):
    def start(self):
        print('Chevrolet Volt running with shocking power!')

    def stop(self):
        print('Chevrolet Volt shutting down.')


class FordFocus(AbsAuto):
    def start(self):
        print('Cool Ford Focus running smoothly.')

    def stop(self):
        print('Ford Focus shutting down.')


class JeepSahara(AbsAuto):
    def start(self):
        print('Jeep Saraha running ruggedly.')

    def stop(self):
        print('Jeep Saraha shutting down.')


class NullCar(AbsAuto):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('Unknown car "%s".' % self._carname)

    def stop(self):
        pass
