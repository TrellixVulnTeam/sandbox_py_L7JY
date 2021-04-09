"""
NQueens problem: Solution by Python
"""
from time import time
from tkinter import *
from tkinter import ttk, messagebox

import nqueens

BG_COLOR = '#e1d8b9'
TEXT_FONT = 'Verdana 10'
TEXT_FONT_B = 'Verdana 10 bold'


class ControlFrame(ttk.Frame):
    def __init__(self, app, **kwargs):
        super().__init__(app.root, **kwargs)

        ttk.Label(self, text='Number of Queens:',
                  font=TEXT_FONT_B).grid(row=0, column=0)
        ttk.Spinbox(self, textvariable=app.n_var, from_=4, to=99,
                    width=2, font=TEXT_FONT_B).grid(row=0, column=1)
        ttk.Button(self, text='Get Next Solution',
                   command=app.solution_callback) \
            .grid(row=1, column=0, columnspan=2, pady=(5, 0))
        ttk.Label(self).grid(row=0, column=2, padx=10)  # spacer
        ttk.Label(self, text='Solution:',
                  font=TEXT_FONT_B).grid(row=0, column=3, sticky=E)
        ttk.Label(self, textvariable=app.solution_var,
                  font=TEXT_FONT).grid(row=0, column=4, sticky=W)
        ttk.Label(self, text='Elapsed Time:',
                  font=TEXT_FONT_B).grid(row=1, column=3, sticky=E)
        ttk.Label(self, textvariable=app.time_var,
                  font=TEXT_FONT).grid(row=1, column=4, sticky=W)


class NQueens:
    """Controller"""

    def __init__(self):
        self.n = 8  # number of queens
        # queens in current solution
        self.queens = tuple(0 for _ in range(self.n))
        self.index = 0  # index of currently displayed solution
        self.solutions = []  # list of all possible solutions for n queens

        # root window
        self.root = Tk()
        self.root.title('NQueens')
        self.root.configure(background=BG_COLOR)
        self.root.minsize(400, 470)
        self.root.resizable(True, True)
        self.root.pack_propagate(False)  # prevent infinite loop on event handling
        self.root.bind('<Configure>', lambda e: self._draw_board())

        # variables
        self.n_var = IntVar(value=self.n)
        self.solution_var = StringVar()
        self.time_var = StringVar()

        # global styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background=BG_COLOR)
        self.style.configure('TButton', font=TEXT_FONT, background=BG_COLOR)
        self.style.configure('TLabel', background=BG_COLOR)

        self.canvas = Canvas(self.root, bg='white')
        self.canvas.pack()

        self.control_frame = ControlFrame(self)
        self.control_frame.pack(pady=10)

        self.solution_callback()  # begin by showing first solution to N queens

    def run(self):
        self.root.mainloop()

    def _draw_board(self):
        self.canvas.delete(ALL)
        maxboardsize = min(self.root.winfo_width(),
                           self.root.winfo_height() - 75)
        cellsize = maxboardsize // self.n
        self.canvas.config(
            height=self.n * cellsize, width=self.n * cellsize)

        # color in black board cells
        for i in range(self.n):
            for j in range(self.n):
                if (i + j + self.n) % 2:  # black cell
                    self.canvas.create_rectangle(
                        i * cellsize, j * cellsize,
                        i * cellsize + cellsize,
                        j * cellsize + cellsize,
                        fill='black')
            # draw a queen (♛:'\u265B')
            self.canvas.create_text(
                i * cellsize + cellsize // 2,
                self.queens[i] * cellsize + cellsize // 2,
                text='♛', font=('Arial', cellsize // 2), fill='red')

    def solution_callback(self):
        try:
            input_val = self.n_var.get()
        except TclError:
            messagebox.showerror(title='Invalid Input',
                                 message='Must enter a number for N.')
            self.n_var.set(self.n)
            return

        # check if N has changed or if this is first run
        if self.n != input_val or self.solutions == []:
            if 4 > input_val:
                messagebox.showerror(title='Invalid Value for N',
                                     message='N must be greater than 4.')
            else:
                self.n = input_val
                self.index = 0
                start_time = time()

                # calculate new list of solutions
                self.solutions = nqueens.nqueens2(self.n)

                elapsed_time = time() - start_time
                self.time_var.set(f'{elapsed_time:.5f}s')
        else:
            self.index += 1

        self.queens = self.solutions[self.index % len(self.solutions)]
        self.solution_var.set(
            f'{self.index % len(self.solutions) + 1}/{len(self.solutions)}')
        self._draw_board()


if __name__ == "__main__":
    NQueens().run()
