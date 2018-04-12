text = """
1 2 3
4 5 6
7 8 9
"""

l = [list(map(int, line.split())) for line in text.splitlines() if line.strip()]
print(l)
print(*l)
print(list(zip(*l)))

# 横の合計
[print(sum(i)) for i in l]

print()

# 縦の合計
[print(sum(i)) for i in list(zip(*l))]
