import sys
import os

print(sys.version_info)
print('Python version {}.{}.{}'.format(*sys.version_info))

print(sys.platform)
print(os.name)

print(os.environ)
print(os.getenv('PATH'))  # os.environ.get(key, default=None)

print(os.getcwd())
print(os.listdir("."))

print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(sys.getdefaultencoding())

print(sys.float_info)

print(sys.path)
