# Python program to illustrate the concept of locks in threading
import threading


def withdraw(lock):
    """function to withdraw from account"""
    global balance
    for _ in range(1000):
        lock.acquire()
        balance -= 1
        lock.release()


def deposit(lock):
    """function to deposit to account"""
    global balance
    for _ in range(2000):
        lock.acquire()
        balance += 1
        lock.release()


def perform_transactions():
    # initial balance (in shared object)
    global balance
    balance = 500

    # creating a lock object
    lock = threading.Lock()

    # creating new processes
    p1 = threading.Thread(target=withdraw, args=(lock,))
    p2 = threading.Thread(target=deposit, args=(lock,))

    # starting processes
    p1.start()
    p2.start()

    # wait until processes are finished
    p1.join()
    p2.join()

    # print final balance
    print("Final balance = {}".format(balance))


if __name__ == "__main__":
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()
