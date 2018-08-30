# "__new__" : customize immutable class's constructor
class ReversedStr(str):
    def __new__(cls, *args, **kwargs):
        self = str.__new__(cls, *args, **kwargs)
        self = self[::-1]
        return self


rs = ReversedStr('hello')
print(rs)
