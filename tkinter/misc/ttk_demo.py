# Tk themed widgets
import tkinter
from tkinter import ttk


class TkinterSample(tkinter.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Test tkinter")
        tkinter.Label(self, text="Label").pack()
        tkinter.Button(self, text="Button").pack()
        tkinter.Checkbutton(self, text="Checkbutton").pack()
        tkinter.Entry(self, text='Entry').pack()
        tkinter.Menubutton(self, text="Menubutton").pack()
        tkinter.Radiobutton(self, text="Radiobutton").pack()
        tkinter.Scale(self).pack()
        tkinter.Scrollbar(self).pack()


class TtkSample(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Test ttk")
        ttk.Label(self, text="Label").pack()
        ttk.Button(self, text="Button").pack()
        ttk.Checkbutton(self, text="Checkbutton").pack()
        ttk.Entry(self, text='Entry').pack()
        ttk.Menubutton(self, text="Menubutton").pack()
        ttk.Radiobutton(self, text="Radiobutton").pack()
        ttk.Scale(self).pack()
        ttk.Scrollbar(self).pack()


if __name__ == "__main__":
    root = tkinter.Tk()

    # tkinter
    TkinterSample(master=root).grid(row=0, column=0, sticky=tkinter.N)

    # ttk
    TtkSample(master=root).grid(row=0, column=1, sticky=tkinter.N)

    root.mainloop()
