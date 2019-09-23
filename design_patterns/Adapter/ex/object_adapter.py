from vendor import Vendor
from adapters import VendAdapter

MOCKVENDORS = (
    VendAdapter(Vendor('Dough Factory', 1, 'Semolina Court')),
    VendAdapter(Vendor('Farm Produce', 14, 'Country Rd.')),
    VendAdapter(Vendor('Cocoa World', 53, 'Tropical Blvd.'))
)

CUSTOMERS = MOCKVENDORS


def main():
    """ Client """
    for cust in CUSTOMERS:
        print('Name: %s; Address: %s' %
              (cust.name, cust.address))


if __name__ == '__main__':
    main()
