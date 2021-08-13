# random, string, argparse

import random
import string
import argparse
import math


def random_uppercase():
    return random.choice(string.ascii_uppercase)


def random_lowercase():
    return random.choice(string.ascii_lowercase)


def random_punctuation():
    return random.choice(string.punctuation)


def random_digit():
    return random.choice(string.digits)


def generate_password(min_length=8, max_length=16, use_punctuation=False):
    length = random.randint(min_length, max_length)

    char_types = 3 if not use_punctuation else 4

    min_count = math.floor(length / char_types)
    char_counts = [min_count for _ in range(char_types)]

    overflow = length - sum(char_counts)

    x = random.sample(range(char_types), overflow)
    for v in x:
        char_counts[v] += 1

    password = [random_uppercase() for _ in range(char_counts[0])]
    password.extend(random_lowercase() for _ in range(char_counts[1]))
    password.extend(random_digit() for _ in range(char_counts[2]))

    if use_punctuation:
        password.extend(random_punctuation() for _ in range(char_counts[3]))

    random.shuffle(password)

    return ''.join(password)


def print_stats(password):
    upper_count = sum(1 for x in password if x in string.ascii_uppercase)
    lower_count = sum(1 for x in password if x in string.ascii_lowercase)
    digit_count = sum(1 for x in password if x in string.digits)
    punctuation_count = sum(1 for x in password if x in string.punctuation)

    print(f"""Password has:
  Uppercase Letters: {upper_count}
  Lowercase Letters: {lower_count}
  Digits: {digit_count}
  Punctuations: {punctuation_count}
""")


def parse_args():
    argparser = argparse.ArgumentParser(
        description='Generate a random password')
    argparser.add_argument('--min_length', '-n', type=int, default=8,
                           help='Minimum length of the password')
    argparser.add_argument('--max_length', '-x', type=int, default=16,
                           help='Maximum length of the password')
    argparser.add_argument('--use_punctuation', dest='punctuation',
                           action='store_true',
                           help='Include special characters in the password')
    argparser.add_argument('--stats', dest='stats', action='store_true',
                           help='Show password stats')
    return argparser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    password = generate_password(
        args.min_length, args.max_length, args.punctuation)

    print(password)

    if args.stats:
        print_stats(password)
