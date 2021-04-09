from tkinter import *


def handle(event):
    print(event)


root = Tk()
root.geometry('320x240+200+200')

root.bind('<Configure>', handle)  # Geometry change

root.bind('<KeyPress>', handle)
# root.bind('<Key>', handle)  # = <KeyPress>
root.bind('<KeyRelease>', handle)

root.bind('<ButtonPress>', handle)
# root.bind('<Button>', handle)  # = <ButtonPress>
# root.bind('<Motion>', handle)  # mouse move
root.bind('<ButtonRelease>', handle)
root.bind('<MouseWheel>', handle)

root.mainloop()
