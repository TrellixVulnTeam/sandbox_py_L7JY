# string format demo


def demo1():
    name = "Hoge Hoge"
    machine = "HAL"
    print('Nice to meet you %s. I am %s' % (name, machine))  # like C printf (legacy)
    print('Nice to meet you {}. I am {}'.format(name, machine))
    print('Nice to meet you {0}. I am {1}'.format(name, machine))
    print("Nice to meet you {name}. I am {machine}".format(name=name, machine=machine))
    print(f'Nice to meet you {name}. I am {machine}')  # 3.6

    v = [1, -2, 3.3]
    print('%4d%10d%10.3f' % (1, -2, 3.3))
    # print('%4d%10d%10.3f' % (*v))  # NG
    print('{0:4}{1:10}{2:10.3f}'.format(*v))
    print('{:4}{:10}{:10.3f}'.format(*v))
    print('{:>04}{:<10}{:10.3f}'.format(*v))


def demo2():
    import math

    x = 1
    for i in range(10):
        x = x * 2
        y = math.sqrt(x)
        # print("{0:4}{1:10}{2:10.3f}".format(i, x, y))
        # print("%4d%10d%10.3f" % (i, x, y))

        # Example of building the format string dynamically
        width1 = 4
        width2 = 10
        width3 = 10

        # Build a format string (two curly brackets get you one curly bracket)
        formatter = "{{0:{0}}}{{1:{1}}}{{2:{2}.3f}}".format(width1, width2, width3)
        print(formatter)  # debug
        print(formatter.format(i, x, y))  # Use the formatter we built

        # There is a more direct way:
        print("{0:{width1}}{1:{width2}}{2:{width3}.3f}".format(i, x, y,
                                                               width1=4, width2=10, width3=10))


def demo3():
    template = "Hi, I'm {name} and I love to eat {food}!"

    def string_factory(values):
        list_of_strings = []
        for item in values:
            list_of_strings.append(template.format(**item))  # unpack
        return list_of_strings

    data = [
        {"name": "Michelangelo", "food": "Pizza"},
        {"name": "Garfield", "food": "Lasagna"}
    ]

    print(string_factory(data))


def demo4():
    foo = "foo"
    bar = 123
    print("Output: {}, {}".format(foo, bar))
    print("Output: {1}, {0}".format(foo, bar))
    print("Output: {var2}, {var1}".format(var1=foo, var2=bar))
    print("Output: {var2:x}, {var2:X}, {var1}".format(var1=foo.upper(), var2=bar))  # x: hexadecimal
    print(f"Output: {bar:b}, {foo.upper()}")  # f-string 3.6

    print()
    product = "Widget"
    price = 19.99
    tax = 0.07
    print(f"{product} has a price of {price}, with tax {tax:.2%}"
          f" the total is {round(price + (price * tax), 2)}")


if __name__ == '__main__':
    print("--- demo1 ---")
    demo1()
    print("\n--- demo2 ---")
    demo2()
    print("\n--- demo3 ---")
    demo3()
    print("\n--- demo4 ---")
    demo4()
