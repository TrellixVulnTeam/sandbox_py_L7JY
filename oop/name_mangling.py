"""
dunder attributes: hidden from other classes
"""


class Foo:
    __secret = "Foo Secret"

    def get_secret(self):
        return Foo.__secret


class Bar(Foo):
    __secret = "Bar Secret"

    # def get_secret(self):
    #     return Bar.__secret


foo = Foo()
# print(foo.__secret)  # NG
print(dir(foo))
print(foo.get_secret())

# name mangling: prevent to be overridden by the sub-classes
print(foo._Foo__secret)

bar = Bar()
print(dir(bar))
print(bar.get_secret())
print(bar._Foo__secret)
print(bar._Bar__secret)
