class User:
    def __init__(self, trusted=False):
        self.trusted = trusted

    def can_login(self):
        return self.trusted


def login(user):
    if user.can_login:  # always True
        print("All our secrets!!! 😨 😩 😱")
    else:
        print("No secrets for you!")


hacker = User(trusted=False)
hacker2 = User(trusted=42)
friend = User(trusted=True)

login(hacker)
login(hacker2)
login(friend)

print('---')


class User:
    def __init__(self, trusted=False):
        self.trusted = trusted

    @property
    def can_login(self):
        return self.trusted


def login(user):
    if user.can_login is True:
        print("All our secrets!!! 😨 😩 😱")
    else:
        print("No secrets for you!")


hacker = User(trusted=False)
hacker2 = User(trusted=42)
friend = User(trusted=True)

login(hacker)
login(hacker2)
login(friend)
