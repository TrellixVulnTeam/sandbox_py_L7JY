class Order(object):
    def __init__(self, shipper):
        self._shipper = shipper

    @property
    def shipper(self):
        return self._shipper


class Shipper(object):
    fedex = 1
    ups = 2
    postal = 3


class ShippingCost(object):
    # inflexible conditional statement
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)
        elif order.shipper == Shipper.postal:
            return self._postal_cost(order)
        else:
            raise ValueError('Invalid shipper %s', order.shipper)

    def _fedex_cost(self, order):
        return 3.00

    def _ups_cost(self, order):
        return 4.00

    def _postal_cost(self, order):
        return 5.00


if __name__ == '__main__':
    # Test Federal Express shipping
    order = Order(Shipper.fedex)
    cost_calulator = ShippingCost()
    cost = cost_calulator.shipping_cost(order)
    assert cost == 3.0

    # Test UPS shipping
    order = Order(Shipper.ups)
    cost_calulator = ShippingCost()
    cost = cost_calulator.shipping_cost(order)
    assert cost == 4.0

    # Test Postal Service shipping
    order = Order(Shipper.postal)
    cost_calulator = ShippingCost()
    cost = cost_calulator.shipping_cost(order)
    assert cost == 5.0

    print('Tests passed')
