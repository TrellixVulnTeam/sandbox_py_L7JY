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
# x --> create the file

DATA = "../data/"
TMP = "../tmp/"

# Open a file
my_file = open(TMP + "scores.txt", "w", encoding="utf-8")

# Show attributes and properties of that file
print("name: " + my_file.name)
print("mode: " + my_file.mode)

# Write to a file
my_file.write("あわわ : 100\nほげ : 99\nふが : 89\n")
my_file.close()

print('---')

# Read the file
my_file = open(TMP + "scores.txt", "r", encoding="utf-8")

# Show attributes and properties of that file
print("name: " + my_file.name)
print("mode: " + my_file.mode)

# Iterate through each line of a file (include line ending)
for line in my_file:
    print(line.rstrip())

my_file.close()

print('---')

# Read the file by pointer (random access)
my_file = open(TMP + "scores.txt", "r", encoding="utf-8")
print("Readline: " + my_file.readline())
print("Readline: " + my_file.readline())
my_file.seek(0)  # rewind to the top
print("Reading...: " + my_file.read(2))
print("Reading again: " + my_file.read(11))
my_file.close()
