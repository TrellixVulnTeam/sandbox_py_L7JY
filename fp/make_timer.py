# nonlocal demo
import time


def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed


if __name__ == '__main__':
    import random

    t = make_timer()

    print(t())  # None
    time.sleep(random.randint(1, 2))
    print(t())
    time.sleep(random.randint(1, 2))
    print(t())
