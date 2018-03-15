#
# Example file for working with filesystem shell methods
#
import os
import shutil
import sys
import time
from datetime import datetime
from os import path

TEXT_FILE = "tmp/textfile.txt"
NEW_FILE = "tmp/newfile.txt"


def main():
    if not path.exists(TEXT_FILE):
        f = open(TEXT_FILE, "w+")
        for i in range(10):
            f.write("This is line %d\n" % (i + 1))
        f.close()

    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    print(sys.platform)

    # Print the name of the OS
    print(os.name)

    print(os.getcwd())
    print(os.getenv('PATH'))
    print(os.listdir("tmp"))

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
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))  # 1個上
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 2個上

    # Get the modification time
    mt = path.getmtime(TEXT_FILE)
    print(mt)
    print(time.ctime(mt))
    print(datetime.fromtimestamp(mt))

    # Calculate how long ago the item was modified
    td = datetime.now() - datetime.fromtimestamp(mt)
    print("It has been " + str(td) + " The file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


def fs_demo():
    # make a duplicate of an existing file
    # get the path to the file in the current directory
    src = path.realpath(TEXT_FILE)

    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    # now use the shell to make a copy of the file
    shutil.copy(src, dst)

    # copy over the permissions, modification times, and other info
    shutil.copystat(src, dst)

    # mkdir
    os.mkdir("./tmp/test")

    # rmdir
    # os.rmdir("test")  # rm dir
    # os.removedirs("test")  # rm -r dir
    shutil.rmtree("./tmp/test")  # rm -rf dir

    # delete file
    if path.exists(NEW_FILE):
        os.unlink(NEW_FILE)

    # rename the original file
    os.rename(TEXT_FILE, NEW_FILE)

    # now put things into a ZIP archive
    if path.exists("tmp"):
        # shutil.make_archive("./tmp/data_arc", "zip", "data")
        shutil.make_archive(base_name="./tmp/data_arc", format="zip", root_dir="data")
        shutil.make_archive(base_name="./tmp/hoge_arc", format="zip", root_dir="data",
                            base_dir="hoge")


def walk_demo():
    for folderName, subfolders, filenames in os.walk('.'):
        print('The current folder is ' + folderName)
        print('Subfolders of ' + folderName + ': ' + str(subfolders))
        print('Files inside ' + folderName + ': ' + str(filenames))
        print()


if __name__ == "__main__":
    main()
    fs_demo()
    walk_demo()
