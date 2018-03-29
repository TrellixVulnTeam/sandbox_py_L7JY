# operator overload


class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        if '.' in self.value:
            return float(self.value) + other
        return int(self.value) + other

    # lhsとrhsを入れ替えて__add__を利用する
    def __radd__(self, other):
        return self + other

    # in place add (+=)
    def __iadd__(self, other):
        self.value = str(self + other)
        return self.value


def main():
    num = NumString(10)
    print(5 + num)
    print(num + 5)
    num += 1
    print(num)


if __name__ == "__main__":
    main()
