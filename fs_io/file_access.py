# Files and File Writing
# modes
# r --> read (default)
# r+ --> read / write
# w --> truncate and write
# w+ --> truncate and read / write
# a --> append
# a+ --> append read / write
# t --> text (default)
# b --> binary

DATA = "../data/"
TMP = "../tmp/"

# Open a file
myFile = open(TMP + "scores.txt", "w", encoding="utf-8")

# Show attributes and properties of that file
print("name: " + myFile.name)
print("mode: " + myFile.mode)

# Write to a file
myFile.write("あわわ : 100\nほげ : 99\nふが : 89\n")
myFile.close()

print('---')

# Read the file
myFile = open(TMP + "scores.txt", "r", encoding="utf-8")  # default: text mode

# Show attributes and properties of that file
print("name: " + myFile.name)
print("mode: " + myFile.mode)

# Iterate through each line of a file (include line ending)
for line in myFile:
    print(line.rstrip())

myFile.close()

print('---')

# Read the file by pointer
myFile = open(TMP + "scores.txt", "r", encoding="utf-8")  # default: text mode
print("Readline: " + myFile.readline())
print("Readline: " + myFile.readline())
myFile.seek(0)  # rewind to the top
print("Reading...: " + myFile.read(2))
print("Reading again: " + myFile.read(11))
myFile.close()
