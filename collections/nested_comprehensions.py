# nested comprehension

# multi-input
values = [x / (x - y) for x in range(10) if x > 5 for y in range(10) if x - y != 0]
print(values)

# values = [x / (x - y)
#           for x in range(10)
#           if x > 5
#           for y in range(10)
#           if x - y != 0]

values = []
for x in range(10):
    if x > 5:
        for y in range(10):
            if x - y != 0:
                values.append(x / (x - y))
print(values)

print()

values = [(x, y) for x in range(5) for y in range(x)]
print(values)

values = []
for x in range(5):
    for y in range(x):
        values.append((x, y))
print(values)

print()

# nested
vals = [[(x, y) for y in range(5)] for x in range(5)]
print(vals)

print()

vals = [[y * 3 for y in range(x)] for x in range(10)]
print(vals)

outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)

print(outer)
