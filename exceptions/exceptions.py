import random

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"


def demo1():
    try:
        dice = random.randint(0, 2)
        if dice == 0:
            last_name = student["last_name"]
            numbered_last_name = 3 + last_name  # TypeError
        elif dice == 1:
            student["hoge"]  # KeyError
        else:
            print("try block end")
    except KeyError as e:
        print(repr(e))
    except TypeError as e:
        print(repr(e))
    except Exception as e:
        print(repr(e))
        raise  # re-raise
    else:
        # no exception
        print("else")
    finally:
        # both
        print("finally")


def demo2():
    s = [1, 4, 6]
    try:
        item = s[5]
    except LookupError:
        print("Handled IndexError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except LookupError:
        print("Handled KeyError")


def demo3():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print(dir(e))
        print("encoding:", e.encoding)
        print("reason:", e.reason)
        print("object:", e.object)
        print("start:", e.start)
        print("end", e.end)


if __name__ == '__main__':
    print(IndexError.__mro__)

    print()
    demo1()
    print()
    demo2()
    print()
    demo3()
