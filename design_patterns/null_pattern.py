import abc


class AbsClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_something(self, value):
        pass


class MyClass(AbsClass):
    def do_something(self, value):
        print('Doing %s.' % value)


class NullClass(AbsClass):
    def do_something(self, value):
        print('Not doing %s.' % value)


class MyObjectFactory:
    @staticmethod
    def create_object(value):
        if value == 'myclass':
            return MyClass()
        else:
            return NullClass()  # instead of "None"


if __name__ == '__main__':
    myobj = MyObjectFactory.create_object('myclass')
    myobj.do_something('something')

    # No need to test the object is None
    # if myobj is not None:
    #     myobj.do_something('something')
    # else:
    #     print('Not doing anything.')

    nullobj = MyObjectFactory.create_object('hogefuga')
    nullobj.do_something('something')
