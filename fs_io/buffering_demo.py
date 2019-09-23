# PyCharm "Run" buffering demo
import sys

for i in range(0, 10):
    print("stdout: " + str(i))
    print("stderr: " + str(i), file=sys.stderr)
