#!/usr/bin/python3

# Scan the file system for ownerless files

import os
import os.path

# Build a set of the UIDs present in /etc/passwd

uidset = set()

for line in open("/etc/passwd"):
    split = line.split(":")
    uidset.add(int(split[2]))

# Alternative implementation
# for user in pwd.getpwall():
# uidset.add(user.pw_uid)

# Walk the specified directory
testdir = "/home/chris"

for folder, dirs, files in os.walk(testdir):
    for file in files:
        # Build the full pathname of the file
        path = folder + "/" + file
        if os.path.islink(path):
            print(path + " is a symlink ... skipping")
            continue
        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            # This will occur if we encounter a broken symlink
            print(path + " not found")
            continue

        if attributes.st_uid not in uidset:
            print(path + " has no owner")
