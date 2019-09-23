import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

DEFAULT_COUNT = 5


class TimerDemo:
    def __init__(self, master):
        self.master = master
        self.setup_master()
        self.frame = ttk.Frame(self.master)
        self.build_grid()
        self.build_banner()
        self.build_entry()
        self.build_timer()
        self.build_buttons()
        self.count_start = self.count = DEFAULT_COUNT
        self.draw_time()
        self.frame.pack(fill=BOTH, expand=True)

    def setup_master(self):
        self.master.title('Timer')
        w, h = 240, 240
        left = (self.master.winfo_screenwidth() - w) // 2
        top = (self.master.winfo_screenheight() - h) // 2
        self.master.geometry(f'{w}x{h}+{left}+{top}')
        self.master.resizable(False, False)

    def build_grid(self):
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=0)

    def build_banner(self):
        banner = ttk.Label(self.frame, text='Timer', anchor=CENTER,
                           foreground='White', background='red',
                           font=('Helvetica', 20))
        banner.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

    def build_entry(self):
        self.entry = ttk.Entry(self.frame)
        self.entry.insert(0, DEFAULT_COUNT)
        self.entry.bind('<Return>', self.entry_listener)
        self.entry.grid(row=1, column=0, sticky='ew', padx=10, pady=10)

    def entry_listener(self, e):
        try:
            self.count_start = self.count = int(self.entry.get())
        except ValueError:
            pass
        else:
            self.draw_time()

    def build_timer(self, *args):
        self.timer = ttk.Label(self.frame, anchor=CENTER,
                               font=('Helvetica', 36))
        self.timer.grid(row=2, column=0, sticky='ew', padx=10, pady=10)

    def build_buttons(self):
        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.grid(row=3, column=0, sticky='ew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        self.start_button = ttk.Button(buttons_frame, text='Start',
                                       command=self.start_timer)
        self.stop_button = ttk.Button(buttons_frame, text='Stop!',
                                      command=self.stop_timer)
        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')
        self.stop_button.config(state=DISABLED)

    def start_timer(self):
        self.stop_button.config(state=NORMAL)
        self.start_button.config(state=DISABLED)
        self.entry.config(state=DISABLED)
        self.countdown()

    def stop_timer(self):
        self.master.after_cancel(self.timer_id)
        self.reset_timer()

    def reset_timer(self):
        self.stop_button.config(state=DISABLED)
        self.start_button.config(state=NORMAL)
        self.entry.config(state=NORMAL)
        self.count = self.count_start
        self.draw_time()

    def draw_time(self):
        m, s = self.count // 60, self.count % 60
        self.timer.config(text=f'{m:0>2}:{s:0>2}')

    def countdown(self):
        self.draw_time()
        if self.count > 0:
            self.count -= 1
            self.timer_id = self.master.after(1000, self.countdown)  # recursive
        else:
            messagebox.showinfo('Time Up!', 'Your timer is Up')
            self.reset_timer()


def main():
    root = Tk()
    TimerDemo(root)
    root.mainloop()


if __name__ == '__main__':
    main()
