import os
import pathlib


print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.path.basename(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(os.path.dirname(__file__)))

print('\n--- pathlib ---')

path = pathlib.Path(__file__)

print(path)
print(path.absolute())
print(path.parent)
print(type(path.parent))
print(path / 'hoge.txt')
