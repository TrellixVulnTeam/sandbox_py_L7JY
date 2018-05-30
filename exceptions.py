import random

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name  # TypeError
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add these two together!")
    print(error)
except Exception:
    print("Unknown error")

print("This code executes!")

print('---')


class MyException(Exception):
    pass


try:
    if random.randint(0, 1):
        raise MyException('Hoge!')
except MyException as e:
    print('exception: ' + str(e))
else:
    # no exception
    print('else')
finally:
    # both
    print('finally')
