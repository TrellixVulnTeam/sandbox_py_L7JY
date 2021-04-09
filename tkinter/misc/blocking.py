# blocking problem
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
root.after(100, task)  # UIを表示させるため少し遅らせる

root.mainloop()
