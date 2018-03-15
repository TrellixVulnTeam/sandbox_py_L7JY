#!/usr/bin/python3

# Program to find prime numbers.
# Intended for demonstrating signals

from time import sleep

# Test for prime number


def isprime(n):
    sleep(0.1)      # 100 msec sleep
    x = 2
    while (x * x) <= n:
        if not n % x:
            return False
        x += 1
    return True


n = 1
primes_list = []

# Build a big list of primes
while True:
    if isprime(n):
        print("%d is prime" % n)
        primes_list.append(n)
    n += 1
