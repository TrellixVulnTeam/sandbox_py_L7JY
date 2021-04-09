from tkinter import *

EXPAND_SIZE = 30
INTERVAL = 10

count = 0
size = 24


# Contract the button
def contract():
    global count, size
    if count > 0:
        size -= 1
        my_button.config(font=("Helvetica", size))
        count -= 1
        root.after(INTERVAL, contract)


# Expand the button
def expand():
    global count, size
    if count >= EXPAND_SIZE:
        contract()
        root.after(500)
        return

    size += 1
    my_button.config(font=("Helvetica", size))
    count += 1
    root.after(INTERVAL, expand)


root = Tk()
root.title("Simple Widget Animation")
root.geometry("400x300")
root.minsize(400, 300)

my_button = Button(root, text="Click Me!", command=expand,
                   font=("Helvetica", size), fg="red")
my_button.pack(expand=True)

root.mainloop()
