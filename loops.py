x = 0
while x < 10:
    print(f"x = {x}")
    x += 1

y = 0
for index in range(10):
    y += index
    print(f"y = {y}")

print()

# use a for loop over a collection
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    print(d)

# using the enumerate() function to get index
for i, d in enumerate(days):
    print(i, d)

print()

# continue & break
student_names = ["James", "Katarina", "Jessica",
                 "Mark", "Bort", "Frank", "Max", ]

for name in student_names:
    if name == "Jessica":
        continue
        print("Found him! " + name)  # unreachable
    if name == "Bort":
        break
    print("Currently testing " + name)

print()

# while-else / for-else
# "break or else"
# breakしなかった場合（ループ完遂あるいは未実行）にelseが実行される
while False:
    print('while loop')
else:
    print('No looping')

n = 0
while n < 5:
    print(n)
    n += 1
else:
    print('completed')

n = 0
while n < 5:
    if n == 2:
        break
    print(n)
    n += 1
else:
    print('quitted by break')

print()

for n in []:
    print('for loop')
else:
    print('No looping')

for n in range(5):
    print(n)
else:
    print('completed')

for n in range(5):
    if n == 2:
        break
    print(n)
else:
    print('quitted by break')
