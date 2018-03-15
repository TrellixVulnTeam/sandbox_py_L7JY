#!/usr/bin/env python3


class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return 'repr: あ the number of bunnies is {}'.format(self._n)

    def __str__(self):
        return 'str: あ the number of bunnies is {}'.format(self._n)


def main():
    s = bunny(47)
    print(s)
    print(repr(s))
    print(ascii(s))

    print(ord('🖖'))
    print(chr(128406))


if __name__ == '__main__':
    main()
