import abc


class AbsState(metaclass=abc.ABCMeta):
    def __init__(self, context):
        self.context = context

    @abc.abstractmethod
    def switch_state(self):
        pass


class State1(AbsState):
    def switch_state(self):
        self.context.state = self.context.state2

    def __str__(self):
        return 'State 1'


class State2(AbsState):
    def switch_state(self):
        self.context.state = self.context.state1

    def __str__(self):
        return 'State 2'


class Context(object):
    def __init__(self):
        self.state1 = State1(self)
        self.state2 = State2(self)
        self.state = self.state1
        self.some_data = {}

    def switch(self):
        self.state.switch_state()

    def __str__(self):
        return str(self.state)


if __name__ == "__main__":
    context = Context()
    print(context)
    context.switch()
    print(context)
