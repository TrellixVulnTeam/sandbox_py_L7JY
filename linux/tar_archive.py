#!/usr/bin/python3

# Archive

import os
import tarfile
import sys


def add_to_archive(f, t):
    """Add file f to archive t"""
    try:
        t.add(f)
    except PermissionError as e:
        print("sorry %s " % e, file=sys.stderr)


file_list = ["."] if len(sys.argv) < 2 else sys.argv[1:]

with tarfile.open("/tmp/test3.tar", "w") as t:
    for file in file_list:
        # os.walk only works on directories
        if os.path.isdir(file):
            for root, dirs, files in os.walk(file):
                for name in files:
                    add_to_archive(root + "/" + name, t)
        # ordinary files are just added individually
        else:
            add_to_archive(file, t)
