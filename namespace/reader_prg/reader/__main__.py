import sys

from . import Reader  # __init__.py

r = Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()
