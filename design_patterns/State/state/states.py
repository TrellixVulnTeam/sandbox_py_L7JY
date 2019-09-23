import abc


class AbsState(metaclass=abc.ABCMeta):
    def __init__(self, context):
        self._cart = context

    @abc.abstractmethod
    def add_item(self):
        pass

    @abc.abstractmethod
    def remove_item(self):
        pass

    @abc.abstractmethod
    def checkout(self):
        pass

    @abc.abstractmethod
    def pay(self):
        pass

    @abc.abstractmethod
    def empty_cart(self):
        pass


class Empty(AbsState):

    def add_item(self):
        self._cart.items += 1
        print('You added the first item')
        self._cart.state = self._cart.not_empty

    def remove_item(self):
        print('Your cart is empty! Nothing to remove!!')

    def checkout(self):
        print("Your cart is empty. Go shopping!")

    def pay(self):
        print("Your cart is empty. How did you get here?")

    def empty_cart(self):
        print("Your cart is already empty.")


class NotEmpty(AbsState):

    def add_item(self):
        self._cart.items += 1
        print('You now have %s items in your cart.' % self._cart.items)

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print('You now have %s items in your cart.' % self._cart.items)
        else:
            print('Your cart is empty again.')
            self._cart.state = self._cart.empty

    def checkout(self):
        print("Done shopping. Let's check out!")
        self._cart.state = self._cart.check_out

    def pay(self):
        print("You have to go to checkout to pay!")

    def empty_cart(self):
        print("Your can only empty the cart at checkout.")


class AtCheckOut(AbsState):

    def add_item(self):
        print("You can't add items at the check out counter.")

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print('You now have %s items in your cart.' % self._cart.items)
        else:
            print('Your cart is empty again.')
            self._cart.state = self._cart.empty

    def checkout(self):
        print("You're already at checkout.")

    def pay(self):
        print("You paid for %s items." % self._cart.items)
        self._cart.state = self._cart.paid_for

    def empty_cart(self):
        self._cart.items = 0
        self._cart.state = self._cart.empty
        print("Your cart is empty again.")


class PaidFor(AbsState):

    def add_item(self):
        print(
            "You already paid for your purchases. Want to shop some more? Get a new shopping cart!")

    def remove_item(self):
        print("You already paid for your purchases and can't remove any.")

    def checkout(self):
        print("Why are you back here?  You already paid!")

    def pay(self):
        print("You already paid.  You can't pay twice!")

    def empty_cart(self):
        print("You paid already. Time to go home!")
