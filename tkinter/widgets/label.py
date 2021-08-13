from tkinter import *
from tkinter import ttk
from PIL import ImageTk

root = Tk()

label = ttk.Label(root, text="Hello, Tkinter!")
label.pack()
print(label.config())

label.config(text='Howdy, Tkinter!')
label.config(relief=RIDGE)
label.config(
    text="Howdy, Tkinter! It's been a really long time since we last met. Great to see you again!")
label.config(width=50)  # characters
label.config(wraplength=300)
label.config(justify=CENTER, anchor=NE)
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 16, 'bold'))

# logo = PhotoImage(file='python_logo.gif')
logo = ImageTk.PhotoImage(file='river.jpg')  # load JPEG using Pillow
label.config(image=logo)
label.config(compound=CENTER)

root.mainloop()
