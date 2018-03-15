# Itertools
import itertools

# Infinite Counting
for x in itertools.count(50, 5):
    print(x)
    if x >= 80:
        break

x = 0
# Infinite Cycling
for c in itertools.cycle([1, 2, 3, 4]):
    print(c)
    x = x + 1
    if x > 20:
        break

x = 0
# Infinite Cycling with string
for c in itertools.cycle("HOGE"):
    print(c)
    x = x + 1
    if x > 20:
        break

x = 0
# Infinite Repeating
for r in itertools.repeat(True):
    print(r)
    x = x + 1
    if x > 10:
        break

# Permutations（順列）: Order matters - some copies with same inputs but in
# different order
# 3P3 = 6
election = {1: "Barb", 2: "Karen", 3: "Erin"}
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)

print()

# Combinations（組み合わせ）: Order does not matter - no copies with same inputs
# 6C3 = 20
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in itertools.combinations(colorsForPainting, 3):
    print(c)
