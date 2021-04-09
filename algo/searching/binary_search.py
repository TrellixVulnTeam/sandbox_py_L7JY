# Binary search
# can only be applied to a sorted list
items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binary_search(item, itemlist):
    # start at the two ends of the list
    lower_idx = 0
    upper_idx = len(itemlist) - 1

    while lower_idx <= upper_idx:
        # calculate the middle point
        mid = (lower_idx + upper_idx) // 2

        # if item is found, return the index
        if itemlist[mid] == item:
            return mid
        # otherwise get the next midpoint
        if item > itemlist[mid]:
            lower_idx = mid + 1
        else:
            upper_idx = mid - 1

    return None


if __name__ == '__main__':
    print(binary_search(23, items))
    print(binary_search(87, items))
    print(binary_search(250, items))
