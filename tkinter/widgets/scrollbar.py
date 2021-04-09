from tkinter import *
from tkinter import ttk

root = Tk()

canvas = Canvas(root, scrollregion=(0, 0, 640, 480), bg='white')
xscroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
yscroll = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
canvas.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
oval = canvas.create_oval(160, 120, 480, 360, fill='red')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

canvas.grid(row=0, column=0, sticky=NSEW)
xscroll.grid(row=1, column=0, sticky=EW)
yscroll.grid(row=0, column=1, sticky=NS)

ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S, E))


def canvas_click(event):
    x = canvas.canvasx(event.x)  # translate to the relative position
    y = canvas.canvasy(event.y)
    canvas.create_oval((x - 5, y - 5, x + 5, y + 5), fill='pink')


canvas.bind('<1>', canvas_click)

root.mainloop()
