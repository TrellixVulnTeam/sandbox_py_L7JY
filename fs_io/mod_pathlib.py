# pathlib.Path (os.PathLike object) demo
from pathlib import Path

print(Path.cwd())
print(Path.home())
print(Path())  # "." : current dir

print()

file_path = Path(__file__)
print(file_path)
print(file_path.absolute())
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.stat())
print(file_path.parent)
print(type(file_path.parent))
print(dir(file_path))

print()

dir_path = Path("../data")
print(dir_path.absolute())
for entry in dir_path.iterdir():
    print(entry.name)

print()

# join path names
print(dir_path / 'hoge.txt')
