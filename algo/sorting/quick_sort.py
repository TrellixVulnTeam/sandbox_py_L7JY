# O(nlogn), in worst case O(n2)
# divide-and-conquer
def quick_sort(dataset, left, right):
    i, j = left, right
    pivot = dataset[(left + right) // 2]
    while i <= j:
        while dataset[i] < pivot:
            i += 1
        while dataset[j] > pivot:
            j -= 1
        if i <= j:
            dataset[i], dataset[j] = dataset[j], dataset[i]
            i += 1
            j -= 1

        # now sort the two partitions
        if j > left:
            quick_sort(dataset, left, j)
        if i < right:
            quick_sort(dataset, i, right)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting:", list1)
    quick_sort(list1, 0, len(list1) - 1)
    print("Finished:", list1)


if __name__ == "__main__":
    main()
