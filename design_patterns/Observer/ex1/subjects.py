import abc

from observers import AbsObserver


# Observables

class AbsSubject(object):
    __metaclass__ = abc.ABCMeta  # python2 style
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.countdown()
            else:
                observer.countdown(value)


class AbsCtxSubject(AbsSubject):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._observers.clear()
