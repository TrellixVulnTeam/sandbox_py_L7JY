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


class MyAdapter(Adaptee, Target):
    def required_function(self):
        self.provided_function_1()
        self.provided_function_2()


class Client:
    def __init__(self, adapter):
        self.adapter = adapter

    def do_something(self):
        self.adapter.required_function()


if __name__ == "__main__":
    adapter = MyAdapter()
    client = Client(adapter)
    client.do_something()
