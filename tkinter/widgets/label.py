from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text="Hello, Tkinter!")
label.pack()
print(label.config())

label.config(text='Howdy, Tkinter!')
label.config(
    text="Howdy, Tkinter! It's been a really long time since we last met. Great to see you again!")
label.config(width=50)  # characters
label.config(wraplength=300)
label.config(justify=CENTER, anchor=NE)
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 16, 'bold'))

logo = PhotoImage(file='python_logo.gif')  # change path to image as necessary
label.config(image=logo)
label.config(compound='text')
label.config(compound='left')
# label.config(compound='center')
# label.config(compound=CENTER)  # constants

label.img = logo
label.config(image=label.img)

root.mainloop()
