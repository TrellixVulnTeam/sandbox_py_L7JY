from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root)
label.pack()

breakfast = StringVar()  # Value holder
breakfast.set('Choose!')

label.config(textvariable=breakfast)

ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack(anchor=W)
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack(anchor=W)
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sausage').pack(anchor=W)
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack(anchor=W)
print(breakfast.get())  # Note: value will be empty if no selection is made

root.mainloop()
