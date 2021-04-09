""" Scope demo
Local
Enclosing
Global
Built-in
"""

# global vs. local variables in functions
x = "global: x"
y = "global: y"


def global_demo():
    # print(x)  # error
    x = "local: x"
    # print(y)  # error
    global y
    y = "local: y"


global_demo()
print(x)
print(y)

print()

print(globals())
globals()['tau'] = 6.283185
print(globals())
print(tau)  # error in IDE, but no problem

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


def report_scope(arg):
    x = 496

    def local_func(): return "Fuga"

    from pprint import pprint as pp
    pp(locals(), width=10)


report_scope(42)
