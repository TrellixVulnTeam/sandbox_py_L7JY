from tkinter import *


def handle(event):
    print('event: {}'.format(event))


root = Tk()
root.geometry('320x240+200+200')

root.bind('<KeyPress>', handle)
root.bind('<KeyRelease>', handle)

root.bind('<ButtonPress>', handle)
root.bind('<ButtonRelease>', handle)
root.bind('<MouseWheel>', handle)

root.mainloop()
