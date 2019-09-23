class Given(object):
    """ Don't touch me """

    def provided_function_1(self):
        print('provided_function_1')

    def provided_function_2(self):
        print('provided_function_2')


class Target:
    def required_function(self):
        # re-implementation
        print('provided_function_1')
        print('provided_function_2')


class Client:
    def __init__(self, some_object):
        self.some_object = some_object

    def do_something(self):
        if self.some_object.__class__ == Given:
            self.some_object.provided_function_1()
            self.some_object.provided_function_2()
        elif self.some_object.__class__ == Target:
            self.some_object.required_function()
        else:
            print("Class of self.some_object not recognized")


if __name__ == "__main__":
    given = Given()
    client = Client(given)
    client.do_something()
    print()
    target = Target()
    client = Client(target)
    client.do_something()
