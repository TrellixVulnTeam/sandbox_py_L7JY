# non blocking using thread
from threading import Thread
from time import sleep
from tkinter import *


def task():
    while running:
        print("Hello")
        sleep(1)


def cancel_task():
    global running
    running = False
    print("Canceled")


root = Tk()

Button(root, text="Push me!", command=cancel_task).pack()

running = True
t = Thread(target=task)
t.start()

root.mainloop()
