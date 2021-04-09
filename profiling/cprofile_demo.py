# Importing the profile module
import cProfile


# we'll check the time consumption of this function
# if our processor is significantly powerful, then the timing will be nearly zero


def squareroot():
    from math import sqrt
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
    print(mylist)


# Running the function for its time consumption
cProfile.run('squareroot()')


# Lets make another function


def selection_sort():
    A = [64, 25, 12, 22, 11]

    for i in range(len(A)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        A[i], A[min_idx] = A[min_idx], A[i]


# Timing the sorting function-
cProfile.run('selection_sort()')
