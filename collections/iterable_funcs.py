import math
from itertools import (groupby, islice, count, chain, accumulate, cycle, repeat,
                       dropwhile, takewhile, combinations, permutations)

# map(), filter()については、fp_demo.py参照

# built-in funcs for iterable
v = ["ab", "abc", "x", "a", "xyz"]
print(min(v, key=len))  # type mismatch but work
print(max(v, key=lambda s: len(s)))
print(sum(range(5)))
print(list(reversed(range(5))))
print(any(len(s) > 2 for s in v))
print(all(len(s) > 2 for s in v))
print(list(zip("ABC", [1, 2, 4])))
print(list(map(ord, "ほげふが")))  # 1 sequence
print(list(map(lambda x, y: x + y, "ほげふが", "ABCD")))  # 2 sequences

print()

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

for i, m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], "=", m[1], "in French")

print()

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for temps in zip(sunday, monday, tuesday):
    print(f"min = {min(temps):4.1f},",
          f"max={max(temps):4.1f},",
          f"average={sum(temps) / len(temps):4.1f}")

print()


# Infinite Counting
def counts():
    for x in count(50, 5):
        yield x
        if x >= 80:
            break


print(list(counts()))


# Infinite Cycling
def cycles(iterable):
    x = 0
    for c in cycle(iterable):
        yield c
        x += 1
        if x > 10:
            break


print(list(cycles([1, 2, 3, 4])))


# Infinite Repeating
def repeats(obj):
    x = 0
    for r in repeat(obj):
        yield r
        x += 1
        if x > 5:
            break


print(list(repeats(True)))

print()


def is_prime(x):
    if x < 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print()

# groupby : need to be sorted
# [("A", 1), ("B", 4), ("A", 2), ("A", 3), ("B", 5)] => [("A", 6), ("B", 9)]
a = [("A", 1), ("B", 4), ("A", 2), ("A", 3), ("B", 5)]

result = [(key, sum(r for _, r in rows)) for key, rows in
          groupby(sorted(a, key=lambda t: t[0]), key=lambda t: t[0])]
print(result)

print()

# Permutations（順列）: Order matters - some copies with same inputs but in different order
# 3P3 = 6
election = {1: "Barb", 2: "Karen", 3: "Erin"}
for p in permutations(election):
    print(p)

for p1 in permutations(election.values()):
    print(p1)

print()

# Combinations（組み合わせ）: Order does not matter - no copies with same inputs
# 4C2 = 6
colorsForPainting = ["Red", "Blue", "Purple", "Orange"]
for c in combinations(colorsForPainting, 2):
    print(c)

print()

primes = islice((x for x in count() if is_prime(x)), 100)
print(primes)
print(list(primes))

print()

print(list(chain([1, 2, 3], [4, 5, 6], [7, 8, 9, 0])))
# flatten
print(list(chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]])))

print()

vals = [30, 20, 10, 40, 100, 50, 40, 30]
print(list(accumulate(vals)))  # default bi-function: sum
print(list(accumulate(vals, max)))
print(list(accumulate(vals, min)))

# dropwhile and takewhile will return values until
# a certain condition is met that stops them
print(list(dropwhile(lambda x: x < 40, vals)))
print(list(takewhile(lambda x: x < 40, vals)))

print()


def sequence():
    """ Generate Recaman's sequence """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


print(list(islice(sequence(), 20)))
