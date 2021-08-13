DATA = "../data/"
TMP = "../tmp/"

# write to file
with open(TMP + "testfile.txt", "w", encoding="utf-8") as f:
    f.write("あわわ : 100\nほげ : 99\nふが : 89\n")

# read file contents at once
with open(TMP + "testfile.txt", "r", encoding="utf-8") as f:
    data = f.read()  # read all into memory
    print(data, end='')

print()

# read file contents line by line
with open(TMP + "testfile.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end='')

print()

# read file contents line by line (readline)
with open(TMP + "testfile.txt", "r", encoding="utf-8") as f:
    # line = f.readline()
    # while line != '':
    #     print(line, end='')
    #     line = f.readline()
    while line := f.readline():  # python3.8
        print(line, end='')

print()

# read file contents into list
with open(TMP + "testfile.txt", "r", encoding="utf-8") as f:
    print(f.readlines())

print()

# Add data to an existing file, and read all from the beginning
with open(TMP + "testfile.txt", "a+", encoding="utf-8") as f:
    f.write("ふぇふぇ : 77\n")
    f.seek(0)
    data = f.read()
    print(data, end='')

print(f.closed)
