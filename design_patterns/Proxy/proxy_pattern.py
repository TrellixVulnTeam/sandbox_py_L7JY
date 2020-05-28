import abc


class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_action(self):
        pass


class RealSubject(Subject):
    """ Don't touch me """

    def do_action(self):
        # do something ...
        pass


class Proxy(Subject):
    def __init__(self, subject):
        self.subject = subject

    def do_action(self):
        # do something ...
        self.subject.do_action()


if __name__ == '__main__':
    o = Proxy(RealSubject())
    o.do_action()
