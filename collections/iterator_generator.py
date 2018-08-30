# Iterator
def fetch(iterator):
    try:
        return next(iterator)
    except StopIteration:
        print("no item")


i = iter([5, 34, 235, 0])  # accepts iterable
print(fetch(i))
print(fetch(i))
print(fetch(i))
print(fetch(i))
print(fetch(i))

print()


# Generator
def gen123():
    input("yield 1:")
    yield 1
    input("yield 2:")
    yield 2
    input("yield 3:")
    yield 3
    print("end")


g = gen123()
print(fetch(g))
print(fetch(g))
print(fetch(g))
print(fetch(g))
