import os


def display_cwd():
    cwd = os.getcwd()
    print("Current Working Directory: ", cwd)


def up_one_directory_level():
    os.chdir("../")


def display_entries_in_directory(directory):
    print(os.listdir(directory))
    with os.scandir(directory) as entries:
        first = next(entries)  # DirEntry object
        print(dir(first))
        print(dir(first.stat()))
        print(first.stat())
        for entry in entries:
            if entry.is_dir():
                prefix = "D:"
            elif entry.is_file():
                prefix = "F:"
            else:
                prefix = "?:"
            print(prefix, entry.name)


if __name__ == "__main__":
    display_cwd()
    up_one_directory_level()
    display_cwd()
    display_entries_in_directory("data/")
