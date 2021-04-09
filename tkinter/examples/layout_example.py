from tkinter import Tk, Toplevel, Text, BOTH, X, LEFT, RIGHT, N, EW, W, NSEW, GROOVE
from tkinter.ttk import Frame, Label, Button, Style, Entry


class Buttons(Toplevel):
    """Pack"""

    def __init__(self, root):
        super().__init__(root)
        self.title("Buttons")
        self.geometry("300x200+10+10")

        Frame(self, relief=GROOVE, borderwidth=1).pack(fill=BOTH, expand=True)
        Button(self, text="Close").pack(side=RIGHT, padx=5, pady=5)
        Button(self, text="OK").pack(side=RIGHT)


class Windows(Toplevel):
    """Grid"""

    def __init__(self, root):
        super().__init__(root)
        self.title("Windows")
        self.geometry("350x300+10-50")
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        Label(self, text="Windows").grid(sticky=W, pady=4, padx=5)
        Text(self).grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=NSEW)
        Button(self, text="Activate").grid(row=1, column=3)
        Button(self, text="Close").grid(row=2, column=3, pady=4)
        Button(self, text="Help").grid(row=5, column=0, padx=5)
        Button(self, text="OK").grid(row=5, column=3)


class Review(Toplevel):
    """Pack"""

    def __init__(self, root):
        super().__init__(root)
        self.title("Review")
        self.geometry("300x300-10+10")

        frame1 = Frame(self)
        frame1.pack(fill=X)
        Label(frame1, text="Title", width=6).pack(side=LEFT, padx=5, pady=5)
        Entry(frame1).pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)
        Label(frame2, text="Author", width=6).pack(side=LEFT, padx=5, pady=5)
        Entry(frame2).pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)
        Label(frame3, text="Review", width=6).pack(side=LEFT, anchor=N, padx=5, pady=5)
        Text(frame3).pack(fill=BOTH, pady=5, padx=5, expand=True)


class Calculator(Toplevel):
    """Grid"""

    def __init__(self, root):
        super().__init__(root)
        self.title("Calculator")
        self.geometry("-10-50")
        for r in range(4):
            self.columnconfigure(r, pad=3)
        for r in range(5):
            self.rowconfigure(r, pad=3)

        Style().configure("TButton", padding=(0, 5, 0, 5), font='Serif 10')

        Entry(self).grid(row=0, columnspan=4, sticky=EW)

        calc_grid = [
            ["Cls", "Back", "", "Close"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for r, row in enumerate(calc_grid):
            for c, text in enumerate(row):
                Button(self, text=text).grid(row=r + 1, column=c)


if __name__ == '__main__':
    root = Tk()
    w, h = 260, 100
    left = (root.winfo_screenwidth() - w) // 2
    top = (root.winfo_screenheight() - h) // 2
    root.geometry(f'{w}x{h}+{left}+{top}')
    root.title("Layout Examples")
    Buttons(root)
    Windows(root)
    Review(root)
    Calculator(root)
    root.mainloop()
