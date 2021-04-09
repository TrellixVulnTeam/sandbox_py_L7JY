from tkinter import *
from tkinter import ttk

root = Tk()

lbox = Listbox(root, height=10)  # not in ttk
lbox.config(selectmode=MULTIPLE)  # browse(default), single, multiple, extended
lbox.grid(column=0, row=0, sticky=(N, W, E, S))

scroll = ttk.Scrollbar(root, orient=VERTICAL, command=lbox.yview)
scroll.grid(column=1, row=0, sticky=(N, S))
lbox.config(yscrollcommand=scroll.set)

# virtual event
lbox.bind('<<ListboxSelect>>', lambda e: print(lbox.curselection()))

ttk.Label(root, text="Status message here", anchor=(W,)).grid(column=0, row=1, sticky=(W, E))
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S, E))

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

for i in range(1, 101):
    lbox.insert(END, 'Line {} of 100'.format(i))

root.mainloop()
