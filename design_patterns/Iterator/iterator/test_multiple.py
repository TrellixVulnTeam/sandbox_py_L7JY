from testdata import employees1, employees2, employees3, departments


def main():
    for o in employees1, employees2, employees3, departments:
        i1 = iter(o)
        i2 = iter(o)
        print(i1 is i2)

        for _ in range(5):
            try:
                print(next(i1).number, end=', ')
                print(next(i2).number)
            except StopIteration:
                print('StopIteration')
                break

        print()


if __name__ == '__main__':
    main()
