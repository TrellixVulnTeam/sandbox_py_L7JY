import abc

from customer import Customer
from vendor import Vendor


class AbsAdapter(metaclass=abc.ABCMeta):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def address(self):
        pass


class CustAdapter(AbsAdapter):
    def name(self):
        return self._adaptee.name

    def address(self):
        return self._adaptee.address


class VendAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return '{} {}'.format(
            self.adaptee.number, self.adaptee.street
        )


class VendorAdapterC(Vendor, Customer):
    """ Customerに合わせる """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return '{} {}'.format(
            self.number, self.street
        )
