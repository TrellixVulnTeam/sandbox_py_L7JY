import datetime


# Iterator
def fetch(iterator):
    try:
        return next(iterator)
    except StopIteration:
        print(">>> no item <<<")


i = iter([5, 34, 235, 0])  # accepts iterable
print(fetch(i))
print(fetch(i))
print(fetch(i))
print(fetch(i))
print(fetch(i))

print()

i = iter(datetime.datetime.now, None)  # 2nd: stop condition: None => infinite
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print()

with open('../data/sample.txt', 'rt') as f:
    for line in iter(lambda: f.readline().strip(), 'END'):
        print(line)
