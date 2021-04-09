# Linear search
# can be used with an unordered list

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_item(needle, haystack):
    for i, e in enumerate(haystack):
        if needle == e:
            return i

    return None


if __name__ == '__main__':
    print(find_item(87, items))
    print(find_item(250, items))
