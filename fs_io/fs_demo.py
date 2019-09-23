#
# Example file for working with filesystem shell methods
#
import os
import shutil
from os import path

DATA = "../data/"
TMP = "../tmp/"
TEXT_FILE = TMP + "textfile.txt"
NEW_FILE = TMP + "newfile.txt"


def fs_demo():
    if not path.exists(TEXT_FILE):
        f = open(TEXT_FILE, "w+")  # truncate and read/write
        for i in range(10):
            f.write("This is line %d\n" % (i + 1))
        f.close()

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
    os.mkdir(TMP + "test")

    # rmdir
    # os.rmdir("test")  # rm dir
    # os.removedirs("test")  # rm -r dir
    shutil.rmtree(TMP + "test")  # rm -rf dir

    # delete file
    if path.exists(NEW_FILE):
        os.unlink(NEW_FILE)

    # rename the original file
    os.rename(TEXT_FILE, NEW_FILE)

    # now put things into a ZIP archive
    if path.exists(TMP):
        # shutil.make_archive(TMP + "data_arc", "zip", "data")
        shutil.make_archive(base_name=TMP + "data_arc", format="zip", root_dir=DATA)
        shutil.make_archive(base_name=TMP + "hoge_arc", format="zip", root_dir=DATA,
                            base_dir="hoge")


if __name__ == "__main__":
    fs_demo()
