# simple-walk-demo.py

import os

DATA = "../data/"

for folder_name, sub_folders, file_names in os.walk(DATA):
    print('The current folder: "' + folder_name + '"')
    print('Sub folders: ' + str(sub_folders))
    print('Files inside: ' + str(file_names))
    print()
