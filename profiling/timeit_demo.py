# Importing timeit module for execution-
import timeit

# Importing square root module-
mysetup = "from math import sqrt"

# code to be measured for execution time
mycode = '''
mylist = []
for x in range(100):
    mylist.append(sqrt(x))
'''

# timeit statement
print(timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=10000))

mycode_2 = 'mylist = [lambda x: sqrt(x) for x in range(100)]'

print(timeit.timeit(setup=mysetup,
                    stmt=mycode_2,
                    number=10000))


selection_sort = '''
A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]
'''

print(timeit.timeit(
    stmt=selection_sort,
    number=10000))

insertion_sort = '''
arr = [64, 25, 12, 22, 11]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
'''

print(timeit.timeit(
    stmt=insertion_sort,
    number=10000))
