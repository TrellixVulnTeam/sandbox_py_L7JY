# Context Manger
# PEP343
import contextlib
import sys


class CtxMgr:
    def __enter__(self):
        print("CtxMgr.__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("CtxMgr.__exit__({}, {}, {})".format(exc_type, exc_val, exc_tb))
        return True  # suppress propagate


@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield "You're in a with-block!"  # __enter__() return value
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit',
              sys.exc_info())
        # raise  # re-raise


@contextlib.contextmanager
def nest_test(name):
    print('Entering:', name)
    yield name
    print('Exiting:', name)


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise


if __name__ == '__main__':
    with CtxMgr() as x:
        print(x)
    with CtxMgr() as x:
        raise Exception("Hoge Hoge")

    def func1(s):
        with CtxMgr() as x:
            return s.upper()

    print(func1("fefe"))

    print()

    with logging_context_manager() as l:
        print(l)
    with logging_context_manager() as l:
        raise Exception("Fuga Fuga")

    print()

    with nest_test('outer') as n1, nest_test('inner nested in ' + n1):
        print("BODY")

    print()

    with propagater("outer", True), propagater("inner", False):
        raise Exception("from Body")
    with propagater("outer", False), propagater("inner", True):
        raise Exception("from Body")
