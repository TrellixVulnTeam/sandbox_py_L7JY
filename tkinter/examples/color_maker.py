# Color Maker
from tkinter import Tk, Frame, Scale, Button, Label, IntVar, BOTH, EW, SOLID

# Preset Colors
COLORS = [
    ("Red", 255, 0, 0), ("Green", 0, 255, 0), ("Blue", 0, 0, 255),
    ("Yellow", 255, 255, 0), ("Magenta", 255, 0, 255), ("Cyan", 0, 255, 255),
]


class Color:
    """Model"""

    def __init__(self):
        # (0, 0, 0)
        self.red = IntVar()
        self.green = IntVar()
        self.blue = IntVar()

    def get_color_str(self):
        return f'#{self.red.get():02x}{self.green.get():02x}{self.blue.get():02x}'

    def get_color_tuple_str(self):
        return f'({self.red.get()}, {self.green.get()}, {self.blue.get()})'

    def set(self, r, g, b):
        """Set a given color"""
        self.red.set(r)
        self.green.set(g)
        self.blue.set(b)


class UiFrame(Frame):
    """View"""

    def __init__(self, root):
        super().__init__(root)
        self.configure(relief=SOLID, padx=10, pady=10)
        self.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Sliders
        for i, name in enumerate(['red', 'green', 'blue']):
            Scale(self, length=256, from_=255, to=0,
                  label=name[0].upper(),
                  variable=getattr(root.color, name),
                  command=root.update_color) \
                .grid(row=0, column=i, sticky=EW)

        for i, c in enumerate(COLORS):
            Button(self, text=c[0], command=lambda x=i: root.set_color(*COLORS[x][1:])) \
                .grid(row=i // 3 + 1, column=i % 3, padx=2, pady=2, sticky=EW)

        # Create the color box and color labels
        color_box = Label(self, bg='black', height=7, width=15)
        self.paint_box = Label(self, bg='black', height=7, width=15)
        self.color_tuple = Label(self, text=root.color.get_color_tuple_str())
        self.color_hex = Label(self, text=root.color.get_color_str())

        # Make the paint_box smaller than the color_box due to ipadx and ipday on the color_box
        color_box.grid(row=0, column=3, columnspan=2, padx=(20, 10),
                       ipadx=10, ipady=10)
        self.paint_box.grid(row=0, column=3, columnspan=2, padx=(20, 10))
        self.color_tuple.grid(row=1, column=3, columnspan=2)
        self.color_hex.grid(row=2, column=3, columnspan=2)


class ColorMaker(Tk):
    """Controller"""

    def __init__(self):
        super().__init__()
        self.title('Color Maker')
        self.resizable(False, False)
        self.color = Color()
        self.ui = UiFrame(self)

    def set_color(self, r, g, b):
        """Set a given color"""
        self.color.set(r, g, b)
        self.update_color()

    def update_color(self, *args):
        """
        Update the paint_box color, tuple string and hex string
        """
        color_string = self.color.get_color_str()
        self.ui.paint_box.config(bg=color_string)
        self.ui.color_tuple.config(text=self.color.get_color_tuple_str())
        self.ui.color_hex.config(text=color_string)


if __name__ == '__main__':
    ColorMaker().mainloop()
