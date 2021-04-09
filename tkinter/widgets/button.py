from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text="Click Me")
button.pack()


def callback(number=None):
    print(f"Clicked! {number if number else 'Top'}")


button.config(command=callback)
button.invoke()  # from code

# button.state(['disabled'])
button.state([DISABLED])  # constants
print(button.instate(['disabled']))
button.state(['!disabled'])
print(button.instate(['disabled']))

logo = PhotoImage(file='python_logo.gif')
button.config(image=logo, compound=LEFT)
small_logo = logo.subsample(5, 5)
button.config(image=small_logo)

# callback
ttk.Button(root, text='Click Me 1', command=lambda: callback(1)).pack()
ttk.Button(root, text='Click Me 2', command=lambda: callback(2)).pack()
ttk.Button(root, text='Click Me 3', command=lambda: callback(3)).pack()

root.mainloop()
