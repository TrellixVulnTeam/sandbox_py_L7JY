# a1, a2 Mandatory
def func1(a1, a2):
    print("func1: " + str(a1) + ", " + str(a2))


# a3, a4 Optional by position or keyword
def func2(a1, a2, a3="hello", a4=42):
    print("func2: " + str(a1) + ", " + str(a2) +
          ", " + str(a3) + ", " + str(a4))


# a3, a4 Optional only by position
def func3(a1, a2, *, a3="hello", a4=42):
    print("func3: " + str(a1) + ", " + str(a2) +
          ", " + str(a3) + ", " + str(a4))
