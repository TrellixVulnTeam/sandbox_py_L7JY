#!/usr/bin/env python3

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(
                'expected at least 1 argument, got {}'.format(numargs))
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(
                'expected at most 3 arguments, got {}'.format(numargs))

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r


class inclusive_range2:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(
                'expected at least 1 argument, got {}'.format(numargs))
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(
                'expected at most 3 arguments, got {}'.format(numargs))

    # ジェネレータ関数を呼び出すと、イテレータを返す
    def __iter__(self):
        # generator
        i = self._start
        while i <= self._stop:
            yield i
            i += self._step


def print_list(iter_obj):
    try:
        for n in iter_obj(25):
            print(n, end=' ')
        print()
    except TypeError as e:
        print('range error: {}'.format(e))


def main():
    print_list(inclusive_range)
    print_list(inclusive_range2)


if __name__ == '__main__':
    main()
