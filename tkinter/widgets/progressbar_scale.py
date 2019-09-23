from tkinter import *
from tkinter import ttk

root = Tk()

pg_indeterminate = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
pg_indeterminate.pack()

pg_indeterminate.config(mode='indeterminate')
pg_indeterminate.start()
# pg_indeterminate.stop()

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar.pack()

progressbar.config(mode='determinate', maximum=11.0, value=4.2)
progressbar.config(value=8.0)
progressbar.step()  # 9
progressbar.step(5)  # wrap back around to 4

value = DoubleVar()
progressbar.config(variable=value)
scale = ttk.Scale(root, orient=HORIZONTAL,
                  length=400, variable=value,
                  from_=0, to=11.0)
scale.pack()
scale.set(4.2)
print(scale.get())

root.mainloop()
