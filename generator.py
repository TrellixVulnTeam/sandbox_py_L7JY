# Generator

students = []


def read_file():
    try:
        f = open("data/students.txt", "r", encoding="utf-8")
        for student in read_students(f):  # 二重ループではない
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


def read_students(f):
    for line in f:
        yield line  #


read_file()
print(students)
