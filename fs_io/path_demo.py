import os

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
this_basename = os.path.basename(__file__)
print(this_basename)
print(os.path.splitext(this_basename))

print(os.path.abspath(os.path.dirname(__file__)))  # 1個上
print(os.path.dirname(os.path.abspath(__file__)))  # 1個上
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 2個上

# join path names
print(os.path.join("/hoge", "fuga", "fefe"))
print(os.path.join("/hoge/", "fuga/", "fefe"))
