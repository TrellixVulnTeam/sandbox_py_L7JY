from tkinter import *
import tkinter.ttk as ttk


class ClipboardDemo(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.input_value = StringVar(value="Clipboard Sample")
        self.output_value = StringVar()
        self.create_widgets()
        self.pack(fill=BOTH)

    def create_widgets(self):
        frame1 = ttk.Frame(self)
        frame1.pack(fill=X)
        entry = ttk.Entry(frame1, textvariable=self.input_value)
        entry.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)
        copy_btn = ttk.Button(frame1, text="Copy", command=self.to_clip)
        copy_btn.pack(padx=5, pady=5)

        frame2 = ttk.Frame(self)
        frame2.pack(fill=X)
        output = ttk.Entry(frame2, textvariable=self.output_value, state="readonly")
        output.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)
        paste_btn = ttk.Button(frame2, text="Paste", command=self.from_clip)
        paste_btn.pack(padx=5, pady=5)

    def to_clip(self):
        self.clipboard_clear()
        self.clipboard_append(self.input_value.get())
        self.from_clip()

    def from_clip(self):
        self.output_value.set(self.clipboard_get())


if __name__ == '__main__':
    master = Tk()
    # master.geometry("300x100")
    master.title("Clipboard Sample")
    ClipboardDemo(master)
    master.mainloop()
