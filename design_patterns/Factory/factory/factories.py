import abc
import sys
from inspect import getmembers, isabstract, isclass

from autos import ChevyVolt, FordFocus, JeepSahara, NullCar


class AbsFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_auto(self):
        pass


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = 'Chevy Volt'
        return chevy


class FordFactory(AbsFactory):
    def create_auto(self):
        self.ford = ford = FordFocus()
        ford.name = 'Ford Focus'
        return ford


class JeepFactory(AbsFactory):
    def create_auto(self):
        self.jeep = jeep = JeepSahara('Jeep Sahara')
        return jeep


class NullFactory(AbsFactory):
    def create_auto(self):
        self.nullcar = nullcar = NullCar()
        nullcar.name = 'Unknown'
        return nullcar


def load_factory(factory_name):
    classes = getmembers(sys.modules[__name__],
                         lambda m: (isclass(m)
                                    and not isabstract(m)
                                    and issubclass(m, AbsFactory))
                         )
    factory_classes = {c[0]: c[1] for c in classes}

    try:
        return factory_classes[factory_name]()
    except KeyError:
        return NullFactory()
