import abc


# Abstract Commands

class AbsCommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass


class AbsOrderCommand(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def description(self):
        pass


# Concrete Commands

class NoCommand(AbsCommand):
    """ Null pattern """
    def __init__(self, args):
        self._command = args[0]

    def execute(self):
        print('No command named %s' % self._command)


class CreateOrder(AbsCommand, AbsOrderCommand):
    name = description = 'CreateOrder'

    def __init__(self, *args):
        pass

    def execute(self):
        print('Create Order...')


class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = 'UpdateQuantity'
    description = 'UpdateQuantity number'

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        self.oldqty = 5
        # Simulate database update
        print('Updated Database')

        # Simulate logging the update
        print('Logging: Updated quantity from %s to %s' % (self.oldqty, self.newqty))


class ShipOrder(AbsCommand, AbsOrderCommand):
    name = description = 'ShipOrder'

    def __init__(self, *args):
        pass

    def execute(self):
        print('Ship Order...')
