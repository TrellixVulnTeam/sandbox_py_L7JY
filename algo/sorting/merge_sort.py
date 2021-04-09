# O(nlogn)
# divide-and-conquer
def merge_sort(dataset):
    if len(dataset) <= 1:  # break point
        return

    mid = len(dataset) // 2
    leftarr = dataset[:mid]
    rightarr = dataset[mid:]

    # recursively break down the arrays
    merge_sort(leftarr)
    merge_sort(rightarr)

    # now perform the merging
    i = 0  # index into the left array
    j = 0  # index into the right array
    k = 0  # index into merged array

    # while both arrays have content
    while i < len(leftarr) or j < len(rightarr):
        if i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
        elif i < len(leftarr):
            # remaining of left
            dataset[k] = leftarr[i]
            i += 1
        else:
            # remaining of right
            dataset[k] = rightarr[j]
            j += 1
        k += 1


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting:", list1)
    merge_sort(list1)
    print("Finished:", list1)


if __name__ == "__main__":
    main()
