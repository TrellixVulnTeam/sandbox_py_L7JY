from tkinter import *
from tkinter import ttk


class App(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.configure(padding="3 3 12 12")
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        self.feet = DoubleVar()
        self.meters = DoubleVar()

        feet_entry = ttk.Entry(self, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self, textvariable=self.meters) \
            .grid(column=2, row=2, sticky=(W, E))
        ttk.Button(self, text="Calculate", command=self.calculate) \
            .grid(column=3, row=3, sticky=W)

        ttk.Label(self, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(self, text="is equivalent to") \
            .grid(column=1, row=2, sticky=E)
        ttk.Label(self, text="meters").grid(column=3, row=2, sticky=W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        feet_entry.bind('<Return>', self.calculate)

    def calculate(self, *args):  # Button（なし）とKeyイベント(あり)への両対応のため、*argsが必要
        try:
            value = float(self.feet.get())
            self.meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except TclError:
            self.feet.set(0)
        except ValueError:
            self.feet.set(0)


def main():
    root = Tk()
    root.title("Feet to Meters")
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
