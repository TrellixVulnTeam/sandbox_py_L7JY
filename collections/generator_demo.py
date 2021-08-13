# Generator
# Generator is Iterator and Iterable
def gen123():
    input("yield 1: press enter")
    yield 1
    input("yield 2: press enter")
    yield 2
    input("yield 3: press enter")
    yield 3
    print("end")


g = gen123()
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # StopIteration
