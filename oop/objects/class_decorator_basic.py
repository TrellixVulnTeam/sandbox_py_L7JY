import inspect


def trace(cls):
    print('*** trace ***')
    print(inspect.getmembers(cls, predicate=inspect.isfunction))
    print(list(filter(lambda item: callable(item[1]), vars(cls).items())))
    return cls


def deco(cls):
    """クラスオブジェクトを引数に取るデコレータ"""
    print('*** deco ***')

    # クラスオブジェクトからメソッド一覧を取得する
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)

    # クラスオブジェクトのメソッドを上書きして回る
    for name, method in methods:
        wrapped_method = logging_wrapper(method)
        setattr(cls, name, wrapped_method)

    return cls


def logging_wrapper(func):
    """関数の呼び出しを記録するデコレータ"""

    def _wrapper(*args, **kwargs):
        print('call:', func.__name__)
        result = func(*args, **kwargs)
        return result

    return _wrapper


# クラスをデコレータでデコレート
@deco
@trace
class MyClass(object):

    def greet_morning(self):
        print('Good morning!')

    def greet_afternoon(self):
        print('Good afternoon!')

    def greet_evening(self):
        print('Good evening!')


def main():
    print('*** __main__ ***')
    o = MyClass()
    o.greet_morning()
    o.greet_afternoon()
    o.greet_evening()


if __name__ == '__main__':
    main()
