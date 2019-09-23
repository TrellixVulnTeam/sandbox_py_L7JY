# Receiver classes


class Appliance(object):
    def __init__(self, name):
        self._name = name

    def on(self):
        print('%s has been turned on.' % self._name)

    def off(self):
        print('%s has been turned off.' % self._name)


class Door(object):
    def __init__(self, name):
        self.name = name

    def lock(self):
        print("%s is locked." % self.name)

    def unlock(self):
        print("%s is unlocked." % self.name)


class Security(object):
    def arm(self):
        print('Security system armed')

    def disarm(self):
        print('Security disarmed')
