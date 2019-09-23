from adapters import VendorAdapterC

MOCKVENDORS = (
    VendorAdapterC('Dough Factory', 1, 'Semolina Court'),
    VendorAdapterC('Farm Produce', 14, 'Country Rd.'),
    VendorAdapterC('Cocoa World', 53, 'Tropical Blvd.')
)

CUSTOMERS = MOCKVENDORS


def main():
    """ Client """
    for cust in CUSTOMERS:
        print('Name: %s; Address: %s' %
              (cust.name, cust.address))


if __name__ == '__main__':
    main()
