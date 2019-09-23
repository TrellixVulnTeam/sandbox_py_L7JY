import abc


class Observer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, observed):
        pass


class ConcreteObserver(Observer):
    def update(self, observed):
        print("Observing: {}".format(observed))


class Observable(object):
    def __init__(self):
        self.observers = set()

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.discard(observer)

    def unregister_all(self):
        self.observers = set()

    def update_all(self):
        for observer in self.observers:
            observer.countdown(self)


if __name__ == "__main__":
    observed = Observable()
    observer1 = ConcreteObserver()
    observed.register(observer1)
    observed.update_all()
