student_names = ["James", "Katarina", "Jessica",
                 "Mark", "Bort", "Frank Grimes", "Max Power", ]

for name in student_names:
    if name == "Bort":
        continue
        print("Found him! " + name)  # unreachable
    print("Currently testing " + name)

x = 0
for index in range(10):
    x += 10
    # print(f"x: {x}")
    print("x: {}".format(x))

while x < 10:
    print("Count is {0}".format(x))
    x += 1

# use a for loop over a collection
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    print(d)

# using the enumerate() function to get index
for i, d in enumerate(days):
    print(i, d)

# else
animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')
for pet in animals:
    # if pet == 'dog': continue
    if pet == 'cat': break
    print(pet)
else:  # breakで抜けたとき以外は実行される
    print('that is all of thianimals')

while False:
    print('loop')
else:
    print('else')
