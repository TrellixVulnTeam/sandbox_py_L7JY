# closure


def outer():
    number = 5

    # closure is pre-defined scope function
    def inner():
        print(number)

    inner()


def close():
    x = 5

    def inner():
        print(x)

    return inner  # return closure ref


# closure = close()
# closure()
close()()  # 即時実行
print(close.__name__)
print(close().__name__)


# call with args
def add_to_five(num):
    def inner():
        print(num + 5)

    return inner


add_to_five(10)()
