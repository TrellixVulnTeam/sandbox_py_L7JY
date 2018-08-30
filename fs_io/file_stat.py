# file stat
import os
import time
from datetime import datetime
from os import path

TEXT_FILE = "../tmp/textfile.txt"


def file_path():
    if not path.exists(TEXT_FILE):
        f = open(TEXT_FILE, "w+")
        for i in range(10):
            f.write("This is line %d\n" % (i + 1))
        f.close()

    # Check for item existence and type
    print("Item exists: " + str(path.exists(TEXT_FILE)))
    print("Item is a file: " + str(path.isfile(TEXT_FILE)))
    print("Item is a directory: " + str(path.isdir(TEXT_FILE)))
    print("Item's size: " + str(path.getsize(TEXT_FILE)))

    # Work with file paths
    src = path.realpath(TEXT_FILE)  # linkを展開する
    print("Item's realpath:", src)
    src = path.abspath(TEXT_FILE)
    print("Item's abspath:", src)
    head, tail = path.split(src)
    print("Item's dirname:", head)
    print("Item's basename:", tail)
    print("Item's dirname:", path.dirname(src))
    print("Item's basename:", path.basename(src))

    # This file
    print(__file__)
    print(path.abspath(__file__))
    print(path.dirname(path.abspath(__file__)))  # 1個上
    print(path.dirname(path.dirname(path.abspath(__file__))))  # 2個上

    # Get the modification time
    mt = path.getmtime(TEXT_FILE)
    print(mt)
    print(time.ctime(mt))
    print(datetime.fromtimestamp(mt))

    # Calculate how long ago the item was modified
    td = datetime.now() - datetime.fromtimestamp(mt)
    print("It has been " + str(td) + " The file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


def list_file_stat():
    for file in os.listdir("."):
        info = os.stat(file)
        print("{0:<30} uid:{1.st_uid:>4}, {1.st_size:>10} byte".format(file, info))


if __name__ == "__main__":
    file_path()
    print()
    list_file_stat()
