from numpy import arange, sin, pi, cos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter


class Plot2D:
    def __init__(self, master):
        self.master = master

        self.phase = 0
        self.t = arange(0.0, 4.0, 0.01)

        # Define matplotlib figure
        f = Figure(figsize=(4, 3), dpi=100)
        self.a = f.add_subplot(111)

        # Tell Tkinter to display matplotlib figure
        self.canvas = FigureCanvasTkAgg(f, master=master)
        self.canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=True)

    def run(self):
        self.update()
        self.master.mainloop()

    def update(self):
        x = 2 * pi * self.t + self.phase
        s = sin(x)
        c = cos(x)
        self.phase += 0.1
        self.a.clear()
        self.a.plot(self.t, s, 'b')
        self.a.plot(self.t, c, 'r')
        self.canvas.draw()
        self.master.after(20, self.update)  # recursive


if __name__ == "__main__":
    root = tkinter.Tk()
    plot = Plot2D(root)
    plot.run()
