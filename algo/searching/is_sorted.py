# determine if a list is sorted
items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted(items):
    # using the all function
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))

    # using the brute force method
    # for i in range(len(items) - 1):
    #     if items[i] > items[i + 1]:
    #         return False
    # return True


if __name__ == '__main__':
    print(is_sorted(items1))
    print(is_sorted(items2))
