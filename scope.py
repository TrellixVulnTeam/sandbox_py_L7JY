# Scope demo


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
    # print(x)  # error
    x = "local: x"
    # print(y)  # error
    global y
    y = "local: y"


someFunction()
print(x)
print(y)

print()

s = "s@global"


# Closure or Lambda
def getfunc2():
    # func = lambda: s  # PEP8 violation
    def func(): return s

    s = "s@getfunc2()"  # 位置に注目
    return func


print(getfunc2()())


# global
def getfunc3():
    def func(): return s

    return func


print(getfunc3()())
