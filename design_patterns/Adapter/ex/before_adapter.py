from customer import Customer
from vendor import Vendor

MOCKCUSTOMERS = (
    Customer('Pizza Love', '33 Pepperoni Lane'),
    Customer('Happy and Green', '25 Kale St.'),
    Customer('Sweet Tooth', '42 Chocolate Ave.')
)

MOCKVENDORS = (
    Vendor('Dough Factory', 1, 'Semolina Court'),
    Vendor('Farm Produce', 14, 'Country Rd.'),
    Vendor('Cocoa World', 53, 'Tropical Blvd.')
)

CUSTOMERS = MOCKCUSTOMERS
VENDORS = MOCKVENDORS

TYPE = 'vendors'


def main():
    if TYPE == 'customers':
        for cust in CUSTOMERS:
            print('Name: %s; Address: %s' %
                  (cust.name, cust.address))
    elif TYPE == 'vendors':
        for vend in VENDORS:
            print('Name: %s; Address: %s %s' %
                  (vend.name, vend.street, vend.street))
    else:
        raise ValueError('Incorrect type: ' + TYPE)


if __name__ == '__main__':
    main()
