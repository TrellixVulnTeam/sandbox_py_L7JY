import os
import sys
from platform import python_version

print(sys.version_info)
print(f'This is python version {python_version()}')

print(sys.platform)
print(os.name)

print(os.environ)
print(os.getenv('PATH'))  # os.environ.get(key, default=None)

print(sys.getdefaultencoding())

print(sys.float_info)

print(sys.path)
