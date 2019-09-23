import abc


class Adaptee(object):
    """ Don't touch me """

    def provided_function_1(self):
        print('provided_function_1')

    def provided_function_2(self):
        print('provided_function_2')


class Target(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def required_function(self):
        pass


class MyAdapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def required_function(self):
        self.adaptee.provided_function_1()
        self.adaptee.provided_function_2()

    def __getattr__(self, attr):
        # Everything else is handled by the wrapped object
        return getattr(self.adaptee, attr)


class Client:
    def __init__(self, adapter):
        self.adapter = adapter

    def do_something(self):
        self.adapter.required_function()


if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = MyAdapter(adaptee)
    client = Client(adapter)
    client.do_something()
