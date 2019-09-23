import abc

from actions import Appliance, Door, Security


# Abstract Command
class AbsCommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


# Appliance Commands

class ApplianceOnCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError
        self.appliance = appliance

    def execute(self):
        self.appliance.on()

    def undo(self):
        self.appliance.off()


class ApplianceOffCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError
        self.appliance = appliance

    def execute(self):
        self.appliance.off()

    def undo(self):
        self.appliance.on()


# Door Commands

class DoorLockCommand(AbsCommand):
    def __init__(self, door):
        if not isinstance(door, Door):
            raise TypeError('Expected a Door object, got %s instead.' % door.__class__.__name__)
        self.door = door

    def execute(self):
        self.door.lock()

    def undo(self):
        self.door.unlock()


class DoorUnlockCommand(AbsCommand):
    def __init__(self, door):
        if not isinstance(door, Door):
            raise TypeError
        self.door = door

    def execute(self):
        self.door.unlock()

    def undo(self):
        self.door.lock()


# Security Commands

class SecurityArmCommand(AbsCommand):
    def __init__(self, security):
        if not isinstance(security, Security):
            raise TypeError
        self.security = security

    def execute(self):
        self.security.arm()

    def undo(self):
        self.security.disarm()


class SecurityDisarmCommand(AbsCommand):
    def __init__(self, security):
        if not isinstance(security, Security):
            raise TypeError
        self.security = security

    def execute(self):
        self.security.disarm()

    def undo(self):
        self.security.arm()
