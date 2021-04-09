import inspect
import datetime
from collections.abc import MutableSequence

print(inspect.ismodule(datetime))
print(inspect.getmembers(datetime))
print(inspect.getmembers(datetime, inspect.isclass))  # 2nd: predicate function
print(inspect.getmembers(datetime.datetime, inspect.isfunction))  # blank for some built-ins

print('---')


class Hoge(MutableSequence):
    def hoge(self, arg=10):
        pass


print(inspect.getmro(Hoge))
print(inspect.getmembers(Hoge, inspect.isclass))
print(inspect.getmembers(Hoge, inspect.isfunction))
signature = inspect.signature(Hoge.hoge)  # callable object
print(repr(signature))
print(signature.parameters)
print(signature.parameters['arg'].default)

print('---')


def num_vowels(text: str) -> int:
    return sum(1 if c.lower() in 'aeiou' else 0
               for c in text)


sig = inspect.signature(num_vowels)
print(repr(sig))
print(sig.parameters['text'])
print(sig.return_annotation)
print(num_vowels.__annotations__)
