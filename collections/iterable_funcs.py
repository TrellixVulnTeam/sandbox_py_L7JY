from itertools import (islice, count, chain, accumulate, cycle, repeat,
                       dropwhile, takewhile, combinations, permutations)
import math

# built-in funcs for iterable
v = ["ab", "abc", "x", "a", "xyz"]
print(min(v, key=len))
print(max(v, key=len))
print(sum([1, 2, 3]))
print(any([False, True, False]))
print(all([False, True, False]))
print(list(zip("ABC", [1, 2, 4])))
print(list(map(ord, "ほげふが")))  # 1 sequence
print(list(map(lambda x, y: x + y, "ほげふが", "ABCD")))  # 2 sequences

print()

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

for i, m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], "=", m[1], "in French")

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
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


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

temperatures = chain([1, 2, 3], [4, 5, 6], [7, 8, 9, 0])
print(all(t > 0 for t in temperatures))

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
