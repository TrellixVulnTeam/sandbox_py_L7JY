""" Scope demo
Local
Enclosing
Global
Built-in
"""


class T:
    lst = ["hoge"]


a = T()
b = T()
c = T()
print(id(a.lst) == id(b.lst))
print(id(a.lst) == id(c.lst))
c.lst = ["c"]
print(id(a.lst) == id(b.lst))
print(id(a.lst) == id(c.lst))

print()

# global vs. local variables in functions
x = "global: x"
y = "global: y"


def someFunction():
    print(x)  # OK


someFunction()


def someFunction2():
    # print(x)  # error
    x = "local: x"
    # print(y)  # error
    global y
    y = "local: y"


someFunction2()
print(x)
print(y)

print()

message = 'global'


def enclosing():
    message = 'enclosing'

    def inner():
        # nonlocal message
        # global message
        message = 'local'

    print('enclosing message:', message)
    inner()
    print('enclosing message:', message)


print('global message:', message)
enclosing()
print('global message:', message)

print()

print(globals())
globals()['tau'] = 6.283185
print(globals())

print()


def report_scope(arg):
    from pprint import pprint as pp
    x = 496
    pp(locals(), width=10)


report_scope(42)


def print_locals():
    name = "Hoge"
    age = 9
    print("{name}: {age}".format(**locals()))


print_locals()
