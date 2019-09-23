import abc


class AbsObserver(object):
    __metaclass__ = abc.ABCMeta  # python2 style

    @abc.abstractmethod
    def update(self, value):
        pass


# Context Manager
class AbsCtxObserver(AbsObserver):
    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass
