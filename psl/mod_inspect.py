import inspect
import datetime
from collections.abc import MutableSequence


class Hoge(MutableSequence):
    def hoge(self, arg=10):
        pass


print(inspect.ismodule(datetime))
print(inspect.getmembers(datetime))
print(inspect.getmembers(datetime, inspect.isclass))  # 2nd: predicate function
print(inspect.getmembers(datetime.datetime, inspect.isfunction))  # blank for some built-ins
print(inspect.getmembers(Hoge, inspect.isclass))
print(inspect.getmembers(Hoge, inspect.isfunction))
signature = inspect.signature(Hoge.hoge)
print(signature)
print(signature.parameters)
print(signature.parameters['arg'].default)
