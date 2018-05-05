# Scope demo


class T:
    l = ["hoge"]


a = T()
b = T()
c = T()
print(id(a.l) == id(b.l))
print(id(a.l) == id(c.l))
c.l = ["c"]
print(id(a.l) == id(b.l))
print(id(a.l) == id(c.l))

print()


# global vs. local variables in functions
x = "global: x"
y = "global: y"


def someFunction():
    # print(x)  # error
    x = "local: x"
    global y
    y = "local: y"


someFunction()
print(x)
print(y)

print()


# 未定義
def getfunc3():
    def func(): return s
    return func


f = getfunc3()
s = "value@call"
print(f())


# Closure or Lambda
def getfunc2():
    # func = lambda: s  # PEP8 violation
    def func(): return s
    s = "value@def"  # 位置に注目
    return func


f = getfunc2()
s = "value@call"
print(f())


# 削除
del f
print(f)  # error
