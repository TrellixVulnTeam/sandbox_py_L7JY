# function based Observer


class ConcreteObserver(object):
    def update(self, observed):
        print("Observing: {}".format(observed))


class Observable(object):
    def __init__(self):
        self.callbacks = set()

    def register(self, callback):
        self.callbacks.add(callback)

    def unregister(self, callback):
        self.callbacks.discard(callback)

    def unregister_all(self):
        self.callbacks = set()

    def update_all(self):
        for callback in self.callbacks:
            callback(self)


if __name__ == "__main__":
    observed = Observable()
    observer1 = ConcreteObserver()
    observed.register(lambda x: observer1.update(x))
    observed.register(lambda x: print("Observing: {}".format(x)))
    observed.update_all()
