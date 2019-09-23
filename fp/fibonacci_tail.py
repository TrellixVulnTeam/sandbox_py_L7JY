# fibonacci sequence by tail call recursion
from tramp import tramp


def f(n, curr=0, next=1):
    if n == 0:
        return curr
    else:
        return f(n - 1, next, curr + next)


print([f(i) for i in range(10)])
# print(tramp(f, 1000))  # NG: RecursionError


def f(n, curr=0, next=1):
    if n == 0:
        yield curr
    else:
        yield f(n - 1, next, curr + next)


print([tramp(f, i) for i in range(10)])
print(tramp(f, 1000))
