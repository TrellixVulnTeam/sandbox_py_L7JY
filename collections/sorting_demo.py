class Product:
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discount_price(self):
        return self.price - (self.price * self.discount)


# the key parameter can be used to sort complex objects
def demo1():
    prod_list = [
        Product("Doohickey", 40, 10, 0.15),
        Product("Widget", 50, 10, 0.05),
        Product("Doohickey", 40, 8, 0.15),
        Product("Thingamabob", 35, 12, 0.0),
        Product("Gadget", 65, 7, 0.20)
    ]

    # use the key parameter to select a field to sort on
    def prodsort(product):
        return product.price

    print(sorted(prod_list, key=prodsort))

    # use the key parameter to select a field to sort on
    print(sorted(prod_list, key=lambda p: p.price))

    # the key parameter can also call a method on the object
    print(sorted(prod_list, key=lambda p: p.discount_price()))

    print()

    # sorting stability guarantees that objects with the same key will
    # have their order preserved even after the data is sorted
    # sort by two different keys, taking advantage of stability
    result = sorted(prod_list, key=lambda p: p.weight)
    print(result)
    print(sorted(result, key=lambda p: p.price, reverse=True))


# the key parameter can be used to sort complex objects
def demo2():
    from operator import attrgetter, methodcaller, itemgetter

    prod_list = [
        Product("Widget A", 50, 10, 0.05),
        Product("Widget B", 40, 8, 0.15),
        Product("Widget C", 35, 12, 0.0),
        Product("Widget D", 65, 7, 0.20),
        Product("Widget E", 70, 7, 0.12)
    ]

    # the operator module functions provide easy ways to select fields
    # attrgetter() retrieves a given attribute or property from an object
    # itemgetter() retrieves an item at a given index in a collection
    # methodcaller() calls the given method on the object
    print("Using the attrgetter method:")
    print(sorted(prod_list, key=attrgetter("weight"), reverse=True))

    print("Using methodcaller to invoke a method:")
    print(sorted(prod_list, key=methodcaller("discount_price")))

    # Use itemgetter to retrieve an index
    inventory = [("Widget A", 5), ("Widget B", 2), ("Widget C", 4),
                 ("Widget D", 7), ("Widget E", 4)]
    print(sorted(inventory, key=itemgetter(1)))


if __name__ == '__main__':
    print("--- demo1 ---")
    demo1()
    print("\n--- demo2 ---")
    demo2()
