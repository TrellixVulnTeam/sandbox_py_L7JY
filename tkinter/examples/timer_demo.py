from tkinter import (Tk, IntVar, StringVar,
                     BOTH, X, CENTER, DISABLED, NORMAL, LEFT, RIGHT)
from tkinter.ttk import Frame, Label, Spinbox, Button

MAX_COUNT = 3600  # sec
DEFAULT_COUNT = 5
WIDTH, HEIGHT = 240, 180


class TimerUi:
    """View"""

    def __init__(self, app):
        self.time_label = Label(app.root, textvariable=app.time, anchor=CENTER,
                                foreground='black', background='lightgray',
                                font=('Helvetica', 60))
        self.time_label.pack(fill=BOTH, expand=True)

        validate_command = (app.root.register(self.check), '%P')
        self.entry = Spinbox(app.root, from_=1, to=MAX_COUNT,
                             textvariable=app.count_start,
                             validate='all',
                             validatecommand=validate_command)
        self.entry.pack(fill=X)
        self.entry.focus()

        buttons_frame = Frame(app.root)
        buttons_frame.pack(fill=X)
        self.start_button = Button(buttons_frame, text='Start',
                                   command=app.start_timer)
        self.stop_button = Button(buttons_frame, text='Stop', state=DISABLED,
                                  command=app.stop_timer)
        self.start_button.pack(side=LEFT, fill=X, expand=True)
        self.stop_button.pack(side=RIGHT, fill=X, expand=True)

    def check(self, new_val):
        return new_val.isdigit() and 1 <= int(new_val) <= MAX_COUNT

    def state_started(self):
        self.stop_button.config(state=NORMAL)
        self.start_button.config(state=DISABLED)
        self.entry.config(state=DISABLED)
        self.time_label.config(foreground='white', background='red')

    def state_stopped(self):
        self.stop_button.config(state=DISABLED)
        self.start_button.config(state=NORMAL)
        self.entry.config(state=NORMAL)
        self.time_label.config(foreground='black', background='lightgray')


class TimerDemo:
    """Controller"""

    def __init__(self):
        self.root = Tk()
        self.root.title('Timer')
        left = (self.root.winfo_screenwidth() - WIDTH) // 2
        top = (self.root.winfo_screenheight() - HEIGHT) // 2
        self.root.geometry(f'{WIDTH}x{HEIGHT}+{left}+{top}')
        self.root.resizable(False, False)

        # variables
        self.count_start = IntVar()
        self.count_start.trace_add('write', self.count_start_changed)
        self.count = IntVar()
        self.count.trace_add('write', self.count_changed)
        self.time = StringVar()
        self.timer_id = None

        self.ui = TimerUi(self)
        self.count_start.set(DEFAULT_COUNT)

    def run(self):
        self.root.mainloop()

    def count_changed(self, *args):
        self.draw_time()

    def count_start_changed(self, *args):
        # Countdown中には呼ばれないようにすること
        self.count.set(self.count_start.get())

    def draw_time(self):
        count = self.count.get()
        m, s = count // 60, count % 60
        self.time.set(f'{m:0>2}:{s:0>2}')

    def start_timer(self):
        if self.count.get() == 0:
            self.count_start_changed()
        self.ui.state_started()
        self.timer_id = self.root.after(1000, self.countdown)

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.ui.state_stopped()

    def countdown(self):
        self.count.set(self.count.get() - 1)
        if self.count.get() > 0:
            self.timer_id = self.root.after(1000, self.countdown)  # recursive
        else:
            self.root.bell()
            self.ui.state_stopped()


if __name__ == '__main__':
    TimerDemo().run()
