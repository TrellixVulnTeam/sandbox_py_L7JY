from testdata import employees1, employees2, employees3, departments


def main():
    print("Employees:")  # Iterator
    print_summary(employees1)
    print()
    print("Employees:")  # Iterable returns normal Iterator
    print_summary(employees2)
    print()
    print("Employees:")  # Iterable returns Generator
    print_summary(employees3)
    print()
    print("Departments:")  # Sequence
    print_summary(departments)


def print_summary(collection):
    for item in collection:
        print('Item Id: {}; Name: {}; Dated: {}'.format(
            item.number, item.name, item.date)
        )


if __name__ == '__main__':
    main()
