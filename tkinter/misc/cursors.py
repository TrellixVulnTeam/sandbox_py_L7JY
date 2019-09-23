from tkinter import *
from tkinter.ttk import Frame, Label, Style


class Example(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.master.title("Cursors")

        style = Style()
        style.configure('TLabel', padding=2)
        style.configure('TFrame', background='pink')

        cursors = ["arrow", "center_ptr", "crosshair", 'tcross', 'hand2',
                   'heart', 'pencil', "fleur", "ibeam", "icon", "none",
                   "sb_h_double_arrow", "sb_v_double_arrow", "watch", "xterm", "no",
                   "starting", "size", "size_ne_sw", "size_ns", "size_nw_se",
                   "size_we", "uparrow", "wait"]
        for item in cursors:
            Label(self, text=item, relief=GROOVE, cursor=item) \
                .pack(fill=BOTH, padx=5, pady=2)

        self.pack()


def main():
    root = Tk()
    root.geometry("+200+50")
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
