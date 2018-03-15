import sys


def remember(thing):
    # file = open("tmp/database.txt", "a")
    # file.write(thing + "\n")
    # file.close
    with open("tmp/database.txt", "a") as file:  # context manager
        file.write(thing + "\n")


def show():
    with open("tmp/database.txt") as file:
        for line in file:
            print(line)


if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        remember(' '.join(sys.argv[1:]))
