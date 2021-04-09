import inspect


def trace(cls):
    """クラスオブジェクトを引数に取るデコレータ"""
    print(inspect.getmembers(cls, predicate=inspect.isfunction))
    print([item for item in vars(cls).items() if callable(item[1])])
    return cls


def deco(cls):
    """クラスオブジェクトを引数に取るデコレータ"""

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
        result = func(*args, **kwargs)
        print(f"Call: {func.__name__}: '{result}'")
        return result

    return _wrapper


# クラスをデコレータでデコレート
@deco
@trace
class MyClass(object):

    def greet_morning(self):
        return 'Good morning!'

    def greet_afternoon(self):
        return 'Good afternoon!'

    def greet_evening(self):
        return 'Good evening!'


if __name__ == '__main__':
    o = MyClass()
    o.greet_morning()
    o.greet_afternoon()
    o.greet_evening()
