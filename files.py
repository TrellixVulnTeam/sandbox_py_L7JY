# Files and File Writing
# w --> write
# r --> read (default)
# r+ --> read and write
# a --> append
# a+ --> append read and write

# Open a file
myFile = open("./tmp/scores.txt", "w", encoding="utf-8")

# Show attributes and properties of that file
print("Name: " + myFile.name)
print("Mode: " + myFile.mode)

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open("./tmp/scores.txt", "r", encoding="utf-8")  # default: text mode
print("Reading...: " + myFile.read(10))
print("Reading again: " + myFile.read(10))
myFile.close()

print()

# Iterative Files
myFile = open("./tmp/scores.txt", "r", encoding="utf-8")  # default: text mode

# Read one line at a time
print("My one line: " + myFile.readline())
myFile.seek(0)

# Iterate through each line of a file
for line in myFile:
    newHighScorer = line.replace("BBB", "PDJ")
    print(newHighScorer)

myFile.close()

# copy text file
infile = open('./data/lines.txt', 'rt')
outfile = open('./tmp/lines-copy.txt', 'wt')
for line in infile:
    # outfile.writelines(line)
    print(line.rstrip(), file=outfile)
    print('.', end='', flush=True)
outfile.close()  # important
infile.close()

# copy binary file
infile = open('./data/berlin.jpg', 'rb')
outfile = open('./tmp/berlin-copy.jpg', 'wb')
while True:
    buf = infile.read(16384)  # 16kb
    if buf:
        outfile.write(buf)
        print('.', end='', flush=True)
    else:
        break
outfile.close()  # important
infile.close()
