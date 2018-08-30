import random
import sys

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    if random.randint(0, 1):
        last_name = student["last_name"]
        numbered_last_name = 3 + last_name  # TypeError
except KeyError:
    print("Error finding last_name", file=sys.stderr)
except TypeError as error:
    print("I can't add these two together!:", str(error), file=sys.stderr)
except Exception:
    print("Unknown error")
    raise  # re-raise
else:
    # no exception
    print("else")
finally:
    # both
    print("finally")

print('---')


class MyException(Exception):
    """ Custom Exception """
    pass


try:
    raise MyException("From MyException")
except (MyException, ValueError) as e:
    print(type(e), ":", e, file=sys.stderr)
    raise  # re-raise
