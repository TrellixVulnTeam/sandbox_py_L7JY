import sys

import os

print(sys.version_info)
print('Python version {}.{}.{}'.format(*sys.version_info))

print(sys.platform)
print(os.name)

print(os.getenv('PATH'))

print(os.getcwd())

print(os.listdir("."))

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
