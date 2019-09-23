# Playing with file descriptors
import sys

TMP = "../tmp/"

print("this is written to stdout")

print("this is written to stderr", file=sys.stderr)

sys.stderr.write("Hoge!")

# Write to a text file
f = open(TMP + "out1", "w")
print("this is written to out1", file=f)
f.close()

# More pythonic way
with open(TMP + "out2", "w") as f:
    print("this is written to out2", file=f)

# Temporarily redirecting stdout
old_stdout = sys.stdout
with open(TMP + "out3", "w") as f:
    sys.stdout = f
    print("this is written to out3")
sys.stdout = old_stdout
print("stdout is restored")
