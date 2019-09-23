# Create a temporary password using Python
import secrets
import string


# Function to return a temporary password given a length
def generate_temp_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    result = ''.join(secrets.choice(potential_chars) for _ in range(num_chars))
    return result


# Function to return a temporary password and enforce 1 number and 1 uppercase
def generate_better_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    while True:
        result = ''.join(secrets.choice(potential_chars) for _ in range(num_chars))

        # if the password has at least one number and one uppercase char we can stop
        if (any(c.isupper() for c in result)
                and any(c.isdigit() for c in result)):
            break

    return result


# create a temporary password
print(generate_temp_pass(10))

# create a stronger temporary password
print(generate_better_pass(10))

# create a temporary, hard-to-guess URL
result_url = "https://my.example.com?reset="
result_url += secrets.token_urlsafe(15)
print(result_url)


def random_password(length):
    haystack = string.ascii_lowercase + string.ascii_lowercase + string.punctuation
    haystack += string.digits * 2 + string.digits[:6] + string.punctuation[:26]
    return ''.join([secrets.choice(haystack) for _ in range(length)])


print(random_password(10))
print(random_password(20))
