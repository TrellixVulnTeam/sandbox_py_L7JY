import math
import traceback


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError(
            "Slope cannot be vertical") from e  # set __cause__


def main():
    try:
        print(inclination(0, 5))
    except InclinationError as e:
        print(e)
        print(repr(e.__context__))
        print(repr(e.__cause__))

        print(e.__traceback__)
        traceback.print_tb(e.__traceback__)  # stderr
        s = traceback.format_tb(e.__traceback__)
        print(s)

    print("Finished")


if __name__ == '__main__':
    main()
