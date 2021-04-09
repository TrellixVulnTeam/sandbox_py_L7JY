from itertools import groupby
from collections import defaultdict

input_str = "D a B c d c C A E c e B b"
result_str = "(a A) (B B b) (c c C c) (D d) (E e)"

# step by step
list1 = [c for c in input_str if not c == " "]
list2 = [(e.upper(), e) for e in list1]
print(list2)
list3 = sorted(list2, key=lambda t: t[0])
print(list3)
list4 = [list(v) for _, v in groupby(list3, key=lambda t: t[0])]
print(list4)
list5 = [" ".join(x for _, x in v) for v in list4]
print(list5)
result1 = " ".join(f"({y})" for y in list5)
print(result1)

print()

# all in one but so complicated
result2 = " ".join(
    f"({y})" for y in (
        " ".join(x for _, x in v) for _, v in
        groupby(
            sorted(
                ((e.upper(), e) for e in
                 (c for c in input_str if not c == " ")),
                key=lambda t: t[0]
            ),
            key=lambda t: t[0]
        )
    )
)
print(result2)

print()

# by defaultdict
grouped = defaultdict(str)
for c in input_str:
    if not c == " ":
        grouped[c.upper()] += c
print(grouped)

result3 = " ".join(f"({' '.join(grouped[k])})" for k in sorted(grouped))
print(result3)
