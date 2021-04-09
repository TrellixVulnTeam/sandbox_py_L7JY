# O(n2)
def bubble_sort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset) - 1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
                print(dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting:", list1)
    bubble_sort(list1)
    print("Finished:", list1)


if __name__ == "__main__":
    main()
