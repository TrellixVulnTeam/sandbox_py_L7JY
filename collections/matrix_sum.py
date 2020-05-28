text = """
1 2 3
4 5 6
7 8 9
"""

l = [list(map(int, line.split()))
     for line in text.splitlines() if line.strip()]
print(l)
print(list(zip(*l)))  # transpose

# 横の合計
for i in l:
    print(sum(i))

print()

# 縦の合計
for i in zip(*l):
    print(sum(i))
