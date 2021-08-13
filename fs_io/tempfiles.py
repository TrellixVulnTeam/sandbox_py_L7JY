# tempfile Module
import os
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
tempFile.write(b"Save this special number for me: 5678309")  # binary
tempFile.seek(0)

# Read the temporary file
print(tempFile.read())

# Close the temporary file
tempFile.close()

print()

# get information about the temp data environment
print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())

print()

# create a temporary file using mkstemp()
(tempfh, tempfp) = tempfile.mkstemp(".tmp", "testTemp", None, True)
f = os.fdopen(tempfh, "w+t")
f.write('This is some text data')
f.seek(0)
print(f.read())
f.close()
os.remove(tempfp)

print()

# create a temp file using the TemporaryFile class
with tempfile.TemporaryFile(mode="w+t") as tf:
    tf.write('This is some text data')
    tf.seek(0)
    print(tf.read())

print()

# create a temporary directory using the TemporaryDirectory class
with tempfile.TemporaryDirectory() as tdp:
    path = os.path.join(tdp, "tempfile.txt")
    with open(path, "w+t", encoding="utf-8") as tf:
        tf.write("This is a temp file in temp dir")
        tf.seek(0)
        print(tf.read())
