from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root)
label.pack()

breakfast = StringVar()  # Value holder
breakfast.set('Choose!')

label.config(textvariable=breakfast)

ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack(anchor='w')
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack(anchor='w')
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sausage').pack(anchor='w')
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack(anchor='w')
print(breakfast.get())  # Note: value will be empty if no selection is made

root.mainloop()
