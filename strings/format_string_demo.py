# string format demo


def demo1():
    name = "Hoge Hoge"
    machine = "HAL"
    print('Nice to meet you %s. I am %s' % (name, machine))  # like C printf (legacy)
    print('Today is %(month)s %(day)s.' % {'month': 12, 'day': 31})
    print('Nice to meet you {}. I am {}'.format(name, machine))
    print('Nice to meet you {0}. I am {1}'.format(name, machine))
    print("Nice to meet you {name}. I am {machine}".format(name=name, machine=machine))
    print(f'Nice to meet you {name}\\. I am {machine}')  # f-string 3.6
    print(rf'Nice to meet you {name}\\. I am {machine}')  # raw f-string
    print(f'{{escaping braces {machine}}}')  # useful for dynamic templates

    print()
    product = "Widget"
    price = 19.99
    tax = 0.07
    print(f"{product} has a price of {price}, with tax {tax:.2%}"
          f" the total is {round(price + (price * tax), 2)}")

    print()
    v = [1, -2, 3.3]
    print('%4d %10d %10.3f' % (1, -2, 3.3))
    # print('%4d %10d %10.3f' % v)  # NG
    print('%4d %10d %10.3f' % tuple(v))
    print('{0:4} {1:10} {2:10.3f}'.format(*v))
    print('{:4} {:10} {:10.3f}'.format(*v))  # 順番通りなら位置指定は省略できる
    print('{:>04} {:<10} {:10.3f}'.format(*v))  # 右寄せ0埋め, 左寄せ


def demo2():
    foo = 123
    bar = 456
    print(f"Output: {foo:04x}, {bar:04x}, {bar:4X}")  # x: hexadecimal
    print(f"Output: {foo:b}, {foo:08b}")  # b: binary


def demo3():
    # Example of building the format string dynamically
    width = {"w1": 4, "w2": 4, "w3": 10}

    # Build a format string (two curly brackets get you one curly bracket)
    formatter = "{{0:{w1}}} {{1:{w2}}} {{2:{w3}.5f}}".format(**width)
    print(formatter)  # {0:4} {1:4} {2:10.5f}

    import math

    for i in range(1, 6):
        print(formatter.format(i, i * 2, math.sqrt(i)))  # Use the formatter we built


def demo4():
    q = 7.748091e-5
    print(q)
    print(format(q))
    print(format(q, ".2e"))
    print(format(q, "f"))
    print(format(q, ".11f"))
    print(format(q, ">+20.11f"))


if __name__ == '__main__':
    print("--- demo1 ---")
    demo1()
    print("\n--- demo2 ---")
    demo2()
    print("\n--- demo3 ---")
    demo3()
    print("\n--- demo4 ---")
    demo4()
