# Example of accessing the attributes of an object
import os
file = "."
info = os.stat(file)
print("file {0} uid {1.st_uid}, size {1.st_size}".format(file, info))

import math
x = 1
for i in range(10):
    x = x * 2
    y = math.sqrt(x)
    print("{0:4}{1:10}{2:10.3f}".format(i, x, y))
    # print("%4d%10d%10.3f" % (i, x, y))

    # Example of building the format string dynamically
    width1 = 4
    width2 = 10
    width3 = 10

    # Build a format string (two curly brackets get you one curly bracket)
    formatter = "{{0:{0}}}{{1:{1}}}{{2:{2}.3f}}".format(width1, width2, width3)
    print(formatter)  # Debug
    print(formatter.format(i, x, y))  # Use the formatter we built

    # There is a more direct way:
    print("{0:{width1}}{1:{width2}}{2:{width3}.3f}".format(i, x, y,
                                                           width1=4, width2=10, width3=10))
