class Order(object):
    def __init__(self):
        pass


class ShippingCost(object):
    def __init__(self, strategy):
        self._strategy = strategy  # callable

    def shipping_cost(self, order):
        return self._strategy(order)


# strategy functions
def fedex_strategy(order):
    return 3.0


ups_strategy = lambda order: 4.0  # lambda

if __name__ == '__main__':
    order = Order()

    # Test Federal Express shipping
    cost_calulator = ShippingCost(fedex_strategy)
    cost = cost_calulator.shipping_cost(order)
    assert cost == 3.0

    # Test UPS shipping
    cost_calulator = ShippingCost(ups_strategy)
    cost = cost_calulator.shipping_cost(order)
    assert cost == 4.0

    # Test Postal Service shipping
    cost_calulator = ShippingCost(lambda order: 5.0)
    cost = cost_calulator.shipping_cost(order)
    assert cost == 5.0

    print('Tests passed')
