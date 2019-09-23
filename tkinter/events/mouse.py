from tkinter import *
from tkinter import ttk

prev = None


def mouse_press(event):
    global prev
    print('event: {}'.format(event))
    prev = event


def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
    prev = event


root = Tk()

canvas = Canvas(root, width=640, height=480, background='white')
canvas.pack()
canvas.bind('<1>', mouse_press)
canvas.bind('<B1-Motion>', draw)

lb = ttk.Label(root, text="Starting...", background='yellow', anchor=CENTER)
lb.pack(ipadx=40, ipady=40, padx=20, pady=20)
lb.bind('<Enter>', lambda e: lb.configure(text='Moved mouse inside'))
lb.bind('<Leave>', lambda e: lb.configure(text='Moved mouse outside'))
lb.bind('<ButtonPress-1>', lambda e: lb.configure(text='Clicked left mouse button'))
lb.bind('<Button-2>', lambda e: lb.configure(text='Clicked center mouse button'))
lb.bind('<3>', lambda e: lb.configure(text='Clicked right mouse button'))
lb.bind('<Double-1>', lambda e: lb.configure(text='Double clicked'))
lb.bind('<Triple-1>', lambda e: lb.configure(text='Triple clicked'))
lb.bind('<B3-Motion>', lambda e: lb.configure(text=f'right button drag to ({e.x}, {e.y})'))

root.mainloop()
