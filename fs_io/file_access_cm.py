DATA = "../data/"
TMP = "../tmp/"

# write a file
with open(TMP + "testfile.txt", "w", encoding="utf-8") as fp:
    fp.write("あわわ : 100\nほげ : 99\nふが : 89\n")

# read a file's data
with open(TMP + "testfile.txt", "r", encoding="utf-8") as fp:
    data = fp.read()  # read all in memory
    print(data, end='')

print()

# Add data to an existing file, and read all from the beginning
with open(TMP + "testfile.txt", "a+", encoding="utf-8") as fp:
    fp.write("ふぇふぇ : 77\n")
    fp.seek(0)
    data = fp.read()
    print(data, end='')

print(fp.closed)
