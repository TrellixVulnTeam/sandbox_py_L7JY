import abc
from computer import Computer


# Abstract Builder

class AbsBuilder(object):
    __metaclass__ = abc.ABCMeta

    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def install_mainboard(self):
        pass

    @abc.abstractmethod
    def install_hard_drive(self):
        pass

    @abc.abstractmethod
    def install_video_card(self):
        pass


# Concrete Builders

class BudgetBoxBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'IN WIN BP655'

    def build_mainboard(self):
        self._computer.mainboard = 'ASRock AM1H-ITX'
        self._computer.cpu = 'AMD Athlon 5150'
        self._computer.memory = 'Kingston ValueRAM 4GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'WD Blue 1TB'

    def install_video_card(self):
        self._computer.video_card = 'On board'


class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'Coolermaster N300'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core i7-4770'
        self._computer.memory = 'Corsair Vengeance 16GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate 2TB'

    def install_video_card(self):
        self._computer.video_card = 'GeForce GTX 1070'
