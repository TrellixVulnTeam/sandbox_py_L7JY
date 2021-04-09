from tkinter import messagebox, Tk, PhotoImage, Text, END, SW, E, W
from tkinter.ttk import Style, Frame, Label, Entry, Button

BG_COLOR = '#e1d8b9'
INPUT_FONT = ('Arial', 10)


class Header(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.logo = PhotoImage(file='tour_logo.gif')  # keep it in memory
        Label(self, image=self.logo).grid(row=0, column=0, rowspan=2)
        Label(self, text='Thanks for Exploring!', style='Header.TLabel') \
            .grid(row=0, column=1, padx=5)
        Label(self, wraplength=300,
              text=("We're glad you chose Explore California for your recent adventure. "
                    "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(
            row=1, column=1, padx=5)


class Content(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text='Name:').grid(row=0, column=0, padx=5, sticky=SW)
        Label(self, text='Email:').grid(row=0, column=1, padx=5, sticky=SW)
        Label(self, text='Comments:').grid(row=2, column=0, padx=5, sticky=SW)
        self.entry_name = Entry(self, width=24, font=INPUT_FONT)
        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email = Entry(self, width=24, font=INPUT_FONT)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments = Text(self, width=50, height=10, font=INPUT_FONT)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)
        Button(self, text='Submit', command=self.submit) \
            .grid(row=4, column=0, padx=5, pady=5, sticky=E)
        Button(self, text='Clear', command=self.clear) \
            .grid(row=4, column=1, padx=5, pady=5, sticky=W)

    def submit(self):
        print(f'Name: {self.entry_name.get()}')
        print(f'Email: {self.entry_email.get()}')
        print(f'Comments: {self.text_comments.get(1.0, END)}')
        self.clear()
        messagebox.showinfo(title='Explore California Feedback',
                            message='Comments Submitted!')

    def clear(self):
        self.entry_name.delete(0, END)
        self.entry_email.delete(0, END)
        self.text_comments.delete(1.0, END)


class Feedback(Tk):

    def __init__(self):
        super().__init__()
        self.title('Explore California Feedback')
        self.resizable(False, False)
        self.configure(background=BG_COLOR)

        # global styles
        style = Style()
        style.configure('TFrame', background=BG_COLOR)
        style.configure('TButton', background=BG_COLOR)
        style.configure(
            'TLabel', background=BG_COLOR, font=('Arial', 10, 'italic'))
        style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        # UI parts
        Header(self).pack(padx=5, pady=5)
        Content(self).pack(padx=5, pady=5)


if __name__ == "__main__":
    feedback = Feedback()
    feedback.mainloop()
