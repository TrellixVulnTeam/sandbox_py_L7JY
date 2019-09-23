from tkinter import *
from tkinter import font
from tkinter.ttk import Frame, Label


class Example(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.master.title("Fonts")
        txt = "Today is a beautiful day"
        Label(self, text=txt).pack()
        Label(self, text=txt, font="TkDefaultFont").pack()
        Label(self, text=txt, font="TkTextFont").pack()
        Label(self, text=txt, font="TkFixedFont").pack()
        Label(self, text=txt, font="TkMenuFont").pack()
        Label(self, text=txt, font="TkHeadingFont").pack()
        Label(self, text=txt, font="TkCaptionFont").pack()
        Label(self, text=txt, font="TkSmallCaptionFont").pack()
        Label(self, text=txt, font="TkIconFont").pack()
        Label(self, text=txt, font="TkTooltipFont").pack()
        Label(self, text=txt, font=('Times', '20', 'bold', 'italic',)).pack()
        Label(self, text=txt, font=font.Font(family="Monospace")).pack()
        print(font.families())
        self.pack()


def main():
    root = Tk()
    root.geometry("+300+200")
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
