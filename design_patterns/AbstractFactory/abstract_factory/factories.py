import abc

from autos.ford import FordFiesta, FordMustang, LincolnMKS
from autos.gm import ChevySpark, ChevyCamaro, CadillacCTS


class AbsFactory(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def create_economy():
        pass

    @staticmethod
    @abc.abstractmethod
    def create_sport():
        pass

    @staticmethod
    @abc.abstractmethod
    def create_luxury():
        pass


class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()


class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
